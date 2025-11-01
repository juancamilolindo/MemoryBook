import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


def get_db_session():
    """
    Sets up the environment, creates a database engine, and returns a new session.
    This utility assumes the calling script has configured the sys.path correctly.
    """
    # --- Environment Loading ---
    if not os.getenv("DB_URL_LOADED"):
        backend_root_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..")
        )
        ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

        # Try loading .env.ENVIRONMENT first, then .env
        env_files = [f".env.{ENVIRONMENT}", ".env"]
        loaded = False
        for env_file in env_files:
            env_path = os.path.join(backend_root_dir, env_file)
            if os.path.exists(env_path):
                print(f"Loading environment from {env_path}")
                load_dotenv(dotenv_path=env_path)
                loaded = True
                break

        if not loaded:
            print("Warning: .env file not found. Using system environment variables.")

        os.environ["DB_URL_LOADED"] = "true"

    # --- Database Connection ---
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", "5432"))  # Default PostgreSQL port
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST_CLOUD = os.getenv("DB_HOST_CLOUD")  # For Cloud Run

    if not all([DB_USER, DB_PASSWORD, DB_NAME]):
        raise ConnectionError(
            "Database connection details (DB_USER, DB_PASSWORD, DB_NAME) must be set."
        )

    IS_CLOUD_RUN = os.getenv("K_SERVICE") is not None
    connect_args_for_engine = {}

    if IS_CLOUD_RUN:
        connect_args = {"unix_socket": f"/cloudsql/{DB_HOST_CLOUD}"}
        engine_url = URL.create(
            drivername="postgresql+psycopg2",
            username=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            query=connect_args,
        )
    else:
        engine_url = URL.create(
            drivername="postgresql+psycopg2",
            username=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
        )

    engine = create_engine(
        engine_url, pool_pre_ping=True, connect_args=connect_args_for_engine
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal()
