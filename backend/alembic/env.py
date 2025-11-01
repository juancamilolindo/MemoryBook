import importlib
import os
import sys
from urllib.parse import quote_plus

from dotenv import load_dotenv

# Añade la ruta del directorio 'app' al sys.path para que Alembic encuentre los modelos
sys.path.insert(0, os.path.join(os.getcwd(), "app"))

from logging.config import fileConfig

from alembic import context
from db.base import Base  # type: ignore
from sqlalchemy import engine_from_config, pool

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# --- INICIO DEL BLOQUE DE SEGURIDAD ---
if ENVIRONMENT == "production":
    confirm = input(
        "🚨 ESTÁS A PUNTO DE EJECUTAR UNA MIGRACIÓN EN PRODUCCIÓN. 🚨\n"
        "¿Estás absolutamente seguro? Escribe 'si' para continuar: "
    )
    if confirm != "si":
        print("❌ Operación cancelada por el usuario.")
        sys.exit(0)
# --- FIN DEL BLOQUE DE SEGURIDAD ---

# Construye el nombre del archivo .env basado en el entorno
env_file_path = f".env.{ENVIRONMENT}"

# Carga las variables de entorno desde el archivo correspondiente si existe
if os.path.exists(env_file_path):
    load_dotenv(dotenv_path=env_file_path)


# La ruta a 'app' ya fue añadida al sys.path anteriormente
models_path = os.path.join(os.getcwd(), "app", "models")
for file in os.listdir(models_path):
    if file.endswith(".py") and not file.startswith("__"):
        importlib.import_module(f"models.{file.replace('.py', '')}")

# La metadata de la Base ahora contendrá todas las definiciones de tablas.
target_metadata = Base.metadata

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ... (Todo el resto del archivo `env.py` sigue igual)
# (La sección de load_dotenv, run_migrations_offline, etc.)
# ...
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD") or "")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

DB_PASSWORD = DB_PASSWORD.replace("%", "%%")
database_url = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
config.set_main_option("sqlalchemy.url", database_url)


def run_migrations_offline() -> None:
    # ... (código que ya tienes)
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    # ... (código que ya tienes)
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
