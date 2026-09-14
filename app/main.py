import os
import time
import psycopg2
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = FastAPI(
    title="API Clasificador de Commits",
    version="1.0.0",
    description="API de producción para clasificar mensajes de commit usando reglas locales u Ollama, registrando en PostgreSQL."
)

# Configuración de variables de entorno
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "iadb")
DB_USER = os.getenv("DB_USER", "app_ia")
DB_PASSWORD = os.getenv("DB_PASSWORD", "claveApp456")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODELO_OLLAMA = os.getenv("MODELO_OLLAMA", "gemma3:270m")
MOTOR_POR_DEFECTO = os.getenv("MOTOR_POR_DEFECTO", "eco")

# Estructura de los datos de entrada (Payload)
class CommitRequest(BaseModel):
    mensaje: str
    motor: str = MOTOR_POR_DEFECTO

# Función para registrar la inferencia en PostgreSQL usando el rol de privilegios mínimos
def registrar_en_db(motor: str, modelo: str, entrada: str, salida: str, latencia_ms: int):
    try:
        conexion = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conexion.cursor()
        query = """
            INSERT INTO inferencias (motor, modelo, entrada, salida, latencia_ms)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (motor, modelo, entrada, salida, latencia_ms))
        conexion.commit()
        cursor.close()
        conexion.close()
    except Exception as e:
        print(f"Error al registrar en la base de datos: {e}")

# Endpoint de comprobación de salud del sistema
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "modelo": MODELO_OLLAMA,
        "motor_por_defecto": MOTOR_POR_DEFECTO
    }

# Endpoint principal de clasificación de commits
@app.post("/clasificar")
def clasificar_commit(payload: CommitRequest):
    inicio = time.time()
    mensaje = payload.mensaje.lower()
    motor = payload.motor.lower()
    salida = ""

    if motor == "eco":
        # Motor basado en reglas lógicas rápidas
        if "fix" in mensaje or "bug" in mensaje or "arreglar" in mensaje:
            salida = "bugfix"
        elif "feat" in mensaje or "agregar" in mensaje or "nuevo" in mensaje:
            salida = "feature"
        elif "docs" in mensaje or "documentacion" in mensaje:
            salida = "documentation"
        else:
            salida = "refactor"
        
        latencia_ms = int((time.time() - inicio) * 1000)
        
        # Registrar en la base de datos
        registrar_en_db("eco", "reglas-locales", payload.mensaje, salida, latencia_ms)
        
        return {
            "motor": "eco",
            "entrada": payload.mensaje,
            "clasificacion": salida,
            "latencia_ms": latencia_ms
        }

    elif motor == "ollama":
        # Motor basado en el modelo local de IA
        prompt = f"Clasifica el siguiente mensaje de commit en una de estas categorías: bugfix, feature, documentation, refactor. Responde solo con la categoría:\n\nCommit: {payload.mensaje}"
        
        try:
            respuesta_ollama = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODELO_OLLAMA,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=30
            )
            
            if respuesta_ollama.status_code == 200:
                resultado_json = respuesta_ollama.json()
                salida = resultado_json.get("response", "").strip()
            else:
                salida = "error-ollama"
        except Exception as e:
            salida = f"error-conexion: {str(e)}"

        latencia_ms = int((time.time() - inicio) * 1000)
        
        # Registrar en la base de datos
        registrar_en_db("ollama", MODELO_OLLAMA, payload.mensaje, salida, latencia_ms)
        
        return {
            "motor": "ollama",
            "modelo": MODELO_OLLAMA,
            "entrada": payload.mensaje,
            "clasificacion": salida,
            "latencia_ms": latencia_ms
        }
    else:
        raise HTTPException(status_code=400, detail="Motor no válido. Usa 'eco' o 'ollama'.")

# Endpoint para consultar el historial de inferencias registradas
@app.get("/inferencias")
def obtener_inferencias():
    try:
        conexion = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT id, fecha, motor, modelo, entrada, salida, latencia_ms FROM inferencias ORDER BY id DESC LIMIT 10;")
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        
        resultados = []
        for fila in filas:
            resultados.append({
                "id": fila[0],
                "fecha": fila[1],
                "motor": fila[2],
                "modelo": fila[3],
                "entrada": fila[4],
                "salida": fila[5],
                "latencia_ms": fila[6]
            })
        return {"total": len(resultados), "inferencias": resultados}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar la base de datos: {e}")
