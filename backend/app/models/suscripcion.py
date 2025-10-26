from db.base import Base
from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import relationship


class Suscripcion(Base):
    __tablename__ = "suscripciones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)
    precio = Column(Float, nullable=False, default=0.0)
    limite_almacenamiento_mb = Column(Integer, nullable=False, default=1024)
    nivel_plan = Column(Integer, nullable=False, default=0)
    esta_activo = Column(Boolean, default=True)

    usuarios = relationship("Usuario", back_populates="suscripcion")
