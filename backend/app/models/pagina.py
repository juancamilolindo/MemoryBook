import enum

from db.base import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy import Enum as SAEnum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class TipoElemento(str, enum.Enum):
    IMAGEN = "IMAGEN"
    TEXTO = "TEXTO"
    FORMA = "FORMA"


class Pagina(Base):
    __tablename__ = "paginas"

    id = Column(Integer, primary_key=True, index=True)
    numero_pagina = Column(Integer, nullable=False)

    proyecto_id = Column(Integer, ForeignKey("proyectos.id"), nullable=False)
    proyecto = relationship("Proyecto", back_populates="paginas")

    plantilla_origen_id = Column(Integer, ForeignKey("paginas_plantilla.id"))
    plantilla_origen = relationship(
        "PaginaPlantilla", back_populates="paginas_generadas"
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario_modificacion_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario_creador = relationship("Usuario", foreign_keys=[usuario_creacion_id])
    usuario_modificador = relationship(
        "Usuario", foreign_keys=[usuario_modificacion_id]
    )

    elementos = relationship(
        "ElementoPagina", back_populates="pagina", cascade="all, delete-orphan"
    )


class ElementoPagina(Base):
    __tablename__ = "elementos_pagina"

    id = Column(Integer, primary_key=True, index=True)

    pagina_id = Column(Integer, ForeignKey("paginas.id"), nullable=False)
    pagina = relationship("Pagina", back_populates="elementos")

    tipo_elemento = Column(SAEnum(TipoElemento), nullable=False)

    posicion_x = Column(Float, default=0)
    posicion_y = Column(Float, default=0)
    ancho = Column(Float, default=100)
    alto = Column(Float, default=100)
    rotacion = Column(Float, default=0)
    orden_capa = Column(Integer, default=0)

    contenido = Column(JSONB, nullable=False)

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario_modificacion_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario_creador = relationship("Usuario", foreign_keys=[usuario_creacion_id])
    usuario_modificador = relationship(
        "Usuario", foreign_keys=[usuario_modificacion_id]
    )
