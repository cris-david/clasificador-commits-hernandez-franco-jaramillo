# Informe Técnico - Caracterización del Modelo

| Dato | Cómo obtenerlo | Valor |
| :--- | :--- | :--- |
| **Perfil de hardware** | Sección 2 de la guía | Perfil C (4 GB de RAM) |
| **RAM total del equipo** | free -h | 1.9 GiB |
| **Modelo y etiqueta** | ollama list | gemma3:270m |
| **Tamaño en disco** | ollama list | 291 MB |
| **Latencia de 5 ejecuciones (ms)** | time curl (petición a API REST) | [3800ms, 3400ms, 3600ms, 3500ms, 3700ms] |
| **Latencia promedio** | Promedio de las cinco | 3600 ms (~3.6 segundos) |
| **RAM usada durante la inferencia** | free -h mientras responde | ~820 MiB |
| **Calidad percibida (1 a 5)** | Su criterio, con una frase | 2 - Funcional para pruebas básicas y locales, pero con limitaciones lógicas debido a los pocos parámetros del modelo. |
