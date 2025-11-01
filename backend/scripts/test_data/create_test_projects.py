import asyncio
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

from app.models.pagina import ElementoPagina, Pagina, TipoElemento  # noqa: E402
from app.models.proyecto import Proyecto, TipoProyecto  # noqa: E402
from app.models.usuario import Usuario  # noqa: E402
from utils.get_db_session import get_db_session  # noqa: E402

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def create_test_projects():
    """
    Populates the database with initial test projects, pages, and elements.
    """
    db = get_db_session()
    try:
        logger.info("Starting project, page, and element creation..")

        # --- Find or Create User ---
        user = db.query(Usuario).filter(Usuario.email == "jkm1l0@gmail.com").first()
        if not user:
            logger.info("Test user 'jkm1l0@gmail.com' not found. Creating it...")
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
            logger.info(f"Using existing user '{user.email}' with ID: {user.id}")

        # --- Create Project ---
        project_name = "Mi Primer Proyecto de Prueba"
        project = db.query(Proyecto).filter(Proyecto.nombre == project_name).first()
        if not project:
            logger.info(f"Creating test project: '{project_name}'...")
            project = Proyecto(
                nombre=project_name,
                descripcion="Un proyecto de prueba generado automáticamente.",
                tipo_proyecto=TipoProyecto.ALBUM,
                usuario_creacion_id=user.id,
            )
            db.add(project)
            db.commit()
            db.refresh(project)
            logger.info(f"Project '{project.nombre}' created with ID: {project.id}")
        else:
            logger.info(
                f"Project '{project.nombre}' already exists with ID: {project.id}"
            )

        # --- Create Page ---
        page_number = 1
        page = (
            db.query(Pagina)
            .filter(
                Pagina.proyecto_id == project.id, Pagina.numero_pagina == page_number
            )
            .first()
        )
        if not page:
            logger.info(
                f"Creating page {page_number} for project '{project.nombre}'..."
            )
            page = Pagina(
                numero_pagina=page_number,
                proyecto_id=project.id,
                usuario_creacion_id=user.id,
            )
            db.add(page)
            db.commit()
            db.refresh(page)
            logger.info(f"Page {page.numero_pagina} created with ID: {page.id}")
        else:
            logger.info(f"Page {page.numero_pagina} already exists with ID: {page.id}")

        # --- Create Elements (Title and Image) ---
        # Title Element
        title_content = {
            "text": "Título de la Página",
            "font_size": 24,
            "color": "#000000",
        }
        title_element = (
            db.query(ElementoPagina)
            .filter(
                ElementoPagina.pagina_id == page.id,
                ElementoPagina.tipo_elemento == TipoElemento.TEXTO,
                ElementoPagina.contenido == title_content,
            )
            .first()
        )
        if not title_element:
            logger.info("Creating title element...")
            title_element = ElementoPagina(
                pagina_id=page.id,
                tipo_elemento=TipoElemento.TEXTO,
                contenido=title_content,
                usuario_creacion_id=user.id,
            )
            db.add(title_element)
            db.commit()
            db.refresh(title_element)
            logger.info(f"Title element created with ID: {title_element.id}")
        else:
            logger.info(f"Title element already exists with ID: {title_element.id}")

        # Image Element
        image_content = {
            "url": "https://picsum.photos/800/600",
            "alt_text": "Imagen de prueba",
        }
        image_element = (
            db.query(ElementoPagina)
            .filter(
                ElementoPagina.pagina_id == page.id,
                ElementoPagina.tipo_elemento == TipoElemento.IMAGEN,
                ElementoPagina.contenido == image_content,
            )
            .first()
        )
        if not image_element:
            logger.info("Creating image element...")
            image_element = ElementoPagina(
                pagina_id=page.id,
                tipo_elemento=TipoElemento.IMAGEN,
                contenido=image_content,
                usuario_creacion_id=user.id,
            )
            db.add(image_element)
            db.commit()
            db.refresh(image_element)
            logger.info(f"Image element created with ID: {image_element.id}")
        else:
            logger.info(f"Image element already exists with ID: {image_element.id}")

        logger.info("Project, page, and element creation finished successfully.")

    except Exception as e:
        logger.error(
            f"An error occurred during project, page, and element creation: {e}"
        )
        db.rollback()
    finally:
        db.close()
        logger.info("Database session closed.")


def main():
    """Main function to connect to DB and run the test data creation."""
    print(
        "-- Iniciando script de creación de proyectos, páginas y elementos de prueba --"
    )
    asyncio.run(create_test_projects())
    print(
        "- Finalizada script de creación de proyectos, páginas y elementos de prueba -"
    )


if __name__ == "__main__":
    main()
