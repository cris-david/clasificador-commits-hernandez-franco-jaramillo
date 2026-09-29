# Informe Técnico - Clasificador de Commits (API FastAPI y PostgreSQL)

## 1. Sección de Pruebas y Validación del Sistema

A continuación se registran los resultados obtenidos durante la ejecución de las pruebas funcionales, de seguridad, persistencia y disponibilidad del sistema.

| ID | Tipo | Qué se verifica | Resultado Esperado | Obtenido | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P-01** | Funcional | GET `/health` responde | Código 200 y estado ok | Código 200 y `{"status": "ok", "base_datos": "ok"}` | **Éxito** |
| **P-02** | Funcional | POST `/clasificar` con motor eco | Código 200 y tipo correcto | Código 200 y clasificación correcta (ej. `fix`) | **Éxito** |
| **P-03** | Funcional | Motor inválido | Código 400 | Código 400 de error en validación de motor | **Éxito** |
| **P-04** | Acceso | Rol `app_ia` intenta DROP TABLE | Error de permisos | Error de permisos por privilegios mínimos | **Éxito** |
| **P-05** | Conectividad | La API resuelve el host db | Devuelve una IP interna | Conectividad exitosa en red Docker interna | **Éxito** |
| **P-06** | Disponibilidad | Reinicio del contenedor de BD | La API se recupera sola | Reconexión exitosa tras levantar la base de datos | **Éxito** |
| **P-07** | Persistencia | `down` y `up` conservan los datos | Los registros siguen existiendo | Datos persistidos correctamente en el volumen `pgdata` | **Éxito** |
| **P-08** | Carga | 10 usuarios sobre el motor eco | p95 < 800 ms y errores < 5% | Latencia promedio óptima y 0% de errores | **Éxito** |

## 2. Conclusiones
El sistema cumple satisfactoriamente con los requerimientos de la guía, implementando una arquitectura robusta con contenedores aislados, control de calidad de código mediante Ruff, pruebas automatizadas en CI/CD con GitHub Actions y un esquema estricto de seguridad con privilegios mínimos en la base de datos PostgreSQL.
