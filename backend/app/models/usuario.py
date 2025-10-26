from db.base import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    contrasena_hash = Column(String(255), nullable=False)
    nombre_completo = Column(String(255))
    url_imagen_perfil = Column(String(512))
    idioma = Column(String(10), default="es")
    esta_activo = Column(Boolean, default=True)
    esta_verificado = Column(Boolean, default=False)

    ultimo_acceso = Column(DateTime(timezone=True), onupdate=func.now())
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())

    suscripcion_id = Column(Integer, ForeignKey("suscripciones.id"))
    suscripcion = relationship("Suscripcion", back_populates="usuarios")

    # Relaciones que se definirán en otros archivos de modelos
    proyectos_colaborados = relationship(
        "ProyectoColaborador", back_populates="usuario"
    )
    fotos_subidas = relationship("Foto", back_populates="usuario_creador")
    proyectos_creados = relationship("Proyecto", back_populates="usuario_creador")
