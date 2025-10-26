import enum

from db.base import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class EstadoFoto(str, enum.Enum):
    ACTIVA = "ACTIVA"
    ELIMINADA = "ELIMINADA"


class Foto(Base):
    __tablename__ = "fotos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255))
    url_almacenamiento = Column(String(512), nullable=False)
    tamano_archivo_kb = Column(Float)
    ubicacion = Column(String(255))
    fecha_captura = Column(DateTime(timezone=True))
    estado = Column(SAEnum(EstadoFoto), default=EstadoFoto.ACTIVA, nullable=False)

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario_modificacion_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario_creador = relationship(
        "Usuario", back_populates="fotos_subidas", foreign_keys=[usuario_creacion_id]
    )
    usuario_modificador = relationship(
        "Usuario", foreign_keys=[usuario_modificacion_id]
    )
