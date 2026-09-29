# Clasificador de Commits con FastAPI y PostgreSQL

Aplicación backend desarrollada en **FastAPI** que permite clasificar mensajes de commit utilizando un motor basado en reglas (`eco`) o un modelo de lenguaje local, registrando todas las inferencias en una base de datos **PostgreSQL**. Cuenta con pruebas automatizadas (`pytest`), control de calidad de código (`ruff`) y un pipeline de integración continua en **GitHub Actions**.

## 🛠️ Tecnologías Utilizadas
- **Python 3.12** & **FastAPI** (API REST)
- **PostgreSQL 16** (Base de datos relacional)
- **Docker & Docker Compose** (Contenerización)
- **Pytest & HTTPX** (Pruebas unitarias y funcionales)
- **Ruff** (Linter y formateador de código)
- **GitHub Actions** (CI/CD)

---

## 🚀 Instalación y Ejecución Local con Docker Compose

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/cris-david/clasificador-commits-hernandez-franco-jaramillo.git](https://github.com/cris-david/clasificador-commits-hernandez-franco-jaramillo.git)
   cd clasificador-commits-hernandez-franco-jaramillo# clasificador-commits-hernandez-franco-jaramillo
