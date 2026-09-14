# Manual Técnico - Clasificador de Commits

## 1. Arquitectura del Sistema
El sistema está compuesto por tres componentes principales que operan de manera desacoplada:
- **Frontend / Cliente:** Interfaz interactiva de FastAPI (`/docs`) y peticiones HTTP mediante `requests` o `curl`.
- **Backend de Producción:** API desarrollada en **FastAPI** y ejecutada mediante el servidor ASGI **Uvicorn**, la cual gestiona dos motores de clasificación:
  - *Motor Eco:* Clasificación basada en reglas lógicas locales rápidas.
  - *Motor Ollama:* Inferencia local basada en IA utilizando el modelo `gemma3:270m` ejecutado a través de Ollama.
- **Capa de Persistencia:** Base de datos relacional ejecutada en un contenedor Docker (`db-ia`) con PostgreSQL 16 Alpine, optimizada para equipos con restricciones de recursos (Perfil C).

## 2. Seguridad
- **Privilegios Mínimos:** La aplicación web se conecta a PostgreSQL utilizando el rol específico `app_ia`, el cual cuenta únicamente con permisos estrictos de `SELECT` e `INSERT` sobre la tabla `inferencias`, negando explícitamente operaciones destructivas como `UPDATE` o `DELETE`.
- **Aislamiento de Secretos:** Las credenciales de acceso, contraseñas de bases de datos y URLs de los servicios se encuentran externamente almacenadas en el archivo `.env`, el cual es ignorado por Git mediante el `.gitignore` para evitar la exposición pública de información sensible en GitHub.
