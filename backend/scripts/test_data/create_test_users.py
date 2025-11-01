import asyncio
import logging
import os
import sys

from app.db.session import SessionLocal
from app.models.usuario import Usuario

backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.insert(0, backend_dir)


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create_test_users():
    """
    Populates the database with initial test users.
    """
    db = SessionLocal()
    try:
        logger.info("Starting user creation...")

        # --- Create User ---
        user = db.query(Usuario).filter(Usuario.email == "jkm1l0@gmail.com").first()
        if not user:
            logger.info("Creating test user...")
            user = Usuario(
                email="jkm1l0@gmail.com",
                contrasena_hash="fake_password_hash",
                nombre_completo="Juan Camilo Lindo",
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


if __name__ == "__main__":
    asyncio.run(create_test_users())
