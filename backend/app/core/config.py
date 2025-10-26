# app/core/config.py
import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Determina el entorno actual. Por defecto, '''development'''.
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Construye el nombre del archivo .env basado en el entorno
env_file_path = f".env.{ENVIRONMENT}"

# Carga las variables de entorno desde el archivo correspondiente si existe
if os.path.exists(env_file_path):
    load_dotenv(dotenv_path=env_file_path)


class Settings(BaseSettings):
    # Variables de la base de datos
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: str = "3306"
    DB_NAME: str
    DB_HOST: str = "localhost"
    DB_HOST_CLOUD: str | None = None  # El socket de Cloud Run

    # Variable de entorno que Google Cloud setea automáticamente
    K_SERVICE: str | None = None

    # Variable para identificar el entorno
    ENVIRONMENT: str = ENVIRONMENT

    class Config:
        # Pydantic ya no necesita gestionar el archivo, lo hacemos nosotros con dotenv
        pass


# Creamos una única instancia que importaremos en otros archivos
settings = Settings()
