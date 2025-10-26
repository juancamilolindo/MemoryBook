import os
import sys
from urllib.parse import quote_plus

from dotenv import load_dotenv

# Añade la ruta base del proyecto al sys.path para importaciones
sys.path.insert(0, os.getcwd())

from logging.config import fileConfig

from alembic import context
from db.base import Base  # type: ignore
from sqlalchemy import engine_from_config, pool

ENVIRONMENT = os.getenv("ENVIRONMENT", "staging")

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

# La metadata de la Base ahora contendrá todas las definiciones de tablas
# porque el import de app.models cargó todos los archivos.
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
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DB_PASSWORD = DB_PASSWORD.replace("%", "%%")
database_url = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
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
