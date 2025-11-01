import logging
import os
import sys

# --- Robust Path Setup ---
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
backend_dir = os.path.abspath(os.path.join(scripts_dir, ".."))
sys.path.insert(0, scripts_dir)
sys.path.insert(0, backend_dir)
app_dir = os.path.abspath(os.path.join(backend_dir, "app"))
sys.path.insert(0, app_dir)
# --- End Path Setup ---

from app.models.usuario import Usuario  # noqa: E402
from utils.get_db_session import get_db_session  # noqa: E402

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def create_test_users():
    """
    Populates the database with initial test users.
    """
    db = get_db_session()
    try:
        logger.info("Starting user creation...")

        usuarioemail = "gustavosantis@gmail.com"

        # --- Create User ---
        user = db.query(Usuario).filter(Usuario.email == usuarioemail).first()
        if not user:
            logger.info("Creating test user...")
            user = Usuario(
                email=usuarioemail,
                contrasena_hash="fake_password_hash",
                nombre_completo="Gustavo Santis",
                esta_activo=True,
                esta_verificado=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            logger.info(f"User '{user.email}' created with ID: {user.id}")
        else:
            logger.info(f"User '{user.email}' already exists with ID: {user.id}")

        logger.info("User creation finished successfully.")

    except Exception as e:
        logger.error(f"An error occurred during user creation: {e}")
        db.rollback()
    finally:
        db.close()
        logger.info("Database session closed.")


def main():
    """Main function to connect to DB and run the user creation."""
    print("--- Iniciando script de creación de usuarios de prueba ---")
    # Since create_test_users is async, we need an event loop to run it.
    # For a simple script, we can use asyncio.run().
    import asyncio

    asyncio.run(create_test_users())
    print("--- Finalizada script de creación de usuarios de prueba ---")


if __name__ == "__main__":
    main()
