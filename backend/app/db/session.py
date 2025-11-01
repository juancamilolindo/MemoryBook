# app/db/session.py
# Importamos nuestra configuración centralizada
from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

# Extraemos la lógica de si estamos en Cloud Run
IS_CLOUD_RUN = settings.K_SERVICE is not None

print(f"DEBUG: IS_CLOUD_RUN = {IS_CLOUD_RUN}")

# Construimos la URL de conexión y los argumentos del motor
connect_args_for_engine = {}
if IS_CLOUD_RUN:
    # Conexión para Cloud Run usando Socket Unix
    # psycopg2 espera la ruta del socket Unix en el parámetro host.
    # El sufijo .s.PGSQL.5432 es necesario para PostgreSQL.
    unix_socket_path = f"/cloudsql/{settings.DB_HOST_CLOUD}"
    engine_url = URL.create(
        drivername="postgresql+psycopg2",
        username=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=unix_socket_path,
        database=settings.DB_NAME,
    )
    print(f"DEBUG: Cloud Run engine_url: {engine_url}")
    print(f"DEBUG: Cloud Run unix_socket_path: {unix_socket_path}")
else:
    # Conexión para desarrollo local
    engine_url = URL.create(
        drivername="postgresql+psycopg2",
        username=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=int(settings.DB_PORT or 5432),
        database=settings.DB_NAME,
    )
    connect_args_for_engine = {}


# Creamos el motor de SQLAlchemy
engine = create_engine(
    engine_url, pool_pre_ping=True, connect_args=connect_args_for_engine
)

# Creamos la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
