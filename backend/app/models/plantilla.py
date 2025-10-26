from db.base import Base
from models.proyecto import TipoProyecto
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import relationship


class Plantilla(Base):
    __tablename__ = "plantillas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    tipo_plantilla = Column(SAEnum(TipoProyecto), nullable=False)

    paginas_plantilla = relationship(
        "PaginaPlantilla", back_populates="plantilla", cascade="all, delete-orphan"
    )


class PaginaPlantilla(Base):
    __tablename__ = "paginas_plantilla"

    id = Column(Integer, primary_key=True, index=True)
    numero_pagina = Column(Integer, nullable=False)
    diseno_html = Column(Text)  # Contenido HTML base de la plantilla

    plantilla_id = Column(Integer, ForeignKey("plantillas.id"), nullable=False)
    plantilla = relationship("Plantilla", back_populates="paginas_plantilla")

    # Relación para saber qué páginas se han creado a partir de esta plantilla de página
    paginas_generadas = relationship("Pagina", back_populates="plantilla_origen")
