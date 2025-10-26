from sqlalchemy.orm import declarative_base

# Base para todos los modelos de SQLAlchemy
Base = declarative_base()

# Importa todos los modelos para que SQLAlchemy y Alembic los reconozcan.
# Alembic necesita que los modelos estén vinculados a los metadatos de la Base.
