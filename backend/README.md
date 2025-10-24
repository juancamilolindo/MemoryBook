# Backend de MemoryBook

Esta carpeta contiene todo el código de la API del backend, construida con FastAPI.

## Cómo empezar (Entorno de Desarrollo)

Sigue estos pasos para configurar tu entorno de desarrollo local para el backend.

### Prerrequisitos

Asegúrate de tener instalados los siguientes programas en tu sistema:

*   [Python](https://www.python.org/downloads/) (versión 3.12 o superior)
*   [Git](https://git-scm.com/downloads/)

### 1. Clonar el Repositorio (si aún no lo has hecho)

En tu terminal, navega a la carpeta donde guardas tus proyectos (ej. `cd ~/Documents/Projects`). Luego, ejecuta el siguiente comando. Git creará automáticamente una nueva carpeta llamada `MemoryBook` con todo el código.

```bash
git clone https://github.com/juancamilolindo/MemoryBook
cd MemoryBook
```
*Por ejemplo, si ejecutas el comando dentro de `~/Documents/Projects`, la ruta final del proyecto será `~/Documents/Projects/MemoryBook`.*

### 2. Crear y Activar un Entorno Virtual

Esto crea una "burbuja" para el proyecto, evitando conflictos de dependencias con otros proyectos. Es una práctica estándar y muy recomendada que te ahorrará problemas en el futuro.

```bash
# Crear el entorno virtual
python3 -m venv .venv

# Activar en macOS/Linux
source .venv/bin/activate

# Activar en Windows
# .venv\Scripts\activate
```
Sabrás que está activo porque el nombre del entorno (`.venv`) aparecerá en tu terminal.

### 3. Instalar Dependencias

Instala todas las dependencias de producción y desarrollo (para pruebas, linting, etc.) con un solo comando:

```bash
pip install -r backend/requirements-dev.txt
```

### 4. Configurar Pre-commit Hooks

Instala los hooks de Git que ejecutarán `ruff` automáticamente antes de cada commit para asegurar la calidad del código.

```bash
pre-commit install
```
A partir de ahora, `ruff` revisará tu código cada vez que hagas `git commit`.

### 5. Ejecutar la Aplicación Localmente

Puedes ejecutar el servidor de desarrollo de FastAPI con `uvicorn`:

```bash
uvicorn app.main:app --reload --app-dir backend
```

La API estará disponible en `http://127.0.0.1:8000`.

### 6. Ejecutar Pruebas y Linters Manualmente

Aunque los pre-commit hooks se encargan del linting, puedes ejecutar las herramientas manualmente cuando quieras:

```bash
# Ejecutar las pruebas unitarias
pytest backend/

# Verificar el formato y linting con ruff
ruff check .

# Formatear el código con ruff
ruff format .
```
