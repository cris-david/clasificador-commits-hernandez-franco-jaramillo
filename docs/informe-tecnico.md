# Informe Técnico - Caracterización del Modelo Local

| Dato | Cómo obtenerlo | Valor |
|---|---|---|
| Perfil de hardware | Sección 2 de la guía | Perfil B (8 GB RAM) |
| RAM total del equipo | `free -h` | 7.8Gi |
| Modelo y etiqueta | `ollama list` | `qwen2.5:0.5b` |
| Tamaño en disco | `ollama list` | 397 MB |
| Latencia de 5 ejecuciones (ms) | `time curl ...` cinco veces | ~230 ms |
| Latencia promedio | Promedio de las cinco | ~230 ms |
| RAM usada durante la inferencia | `free -h` mientras responde | ~1.8 Gi |
| Calidad percibida (1 a 5) | Su criterio, con una frase que lo justifique | 4/5 - Responde de manera rápida y precisa a instrucciones estructuradas en español. |
