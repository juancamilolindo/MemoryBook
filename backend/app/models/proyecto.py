import enum

from db.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table, Text
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


# --- Enums ---
class TipoProyecto(str, enum.Enum):
    ALBUM = "ALBUM"
    CALENDARIO = "CALENDARIO"


class VisibilidadProyecto(str, enum.Enum):
    PUBLICO = "PUBLICO"
    PRIVADO = "PRIVADO"


class EstadoProyecto(str, enum.Enum):
    ACTIVO = "ACTIVO"
    ARCHIVADO = "ARCHIVADO"


class RolColaborador(str, enum.Enum):
    PROPIETARIO = "PROPIETARIO"
    EDITOR = "EDITOR"
    VISUALIZADOR = "VISUALIZADOR"


# --- Tabla de Asociación para Proyecto-Categoria ---
proyecto_categoria_tabla = Table(
    "proyecto_categoria",
    Base.metadata,
    Column("proyecto_id", Integer, ForeignKey("proyectos.id"), primary_key=True),
    Column("categoria_id", Integer, ForeignKey("categorias.id"), primary_key=True),
)


# --- Modelos Principales ---
class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)

    proyectos = relationship(
        "Proyecto", secondary=proyecto_categoria_tabla, back_populates="categorias"
    )


class Proyecto(Base):
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text)
    tipo_proyecto = Column(SAEnum(TipoProyecto), nullable=False)
    url_imagen_portada = Column(String(512))
    visibilidad = Column(
        SAEnum(VisibilidadProyecto), default=VisibilidadProyecto.PRIVADO, nullable=False
    )
    estado = Column(
        SAEnum(EstadoProyecto), default=EstadoProyecto.ACTIVO, nullable=False
    )

    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_modificacion = Column(DateTime(timezone=True), onupdate=func.now())
    usuario_creacion_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario_modificacion_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario_creador = relationship(
        "Usuario",
        back_populates="proyectos_creados",
        foreign_keys=[usuario_creacion_id],
    )
    usuario_modificador = relationship(
        "Usuario", foreign_keys=[usuario_modificacion_id]
    )

    colaboradores = relationship(
        "ProyectoColaborador", back_populates="proyecto", cascade="all, delete-orphan"
    )
    categorias = relationship(
        "Categoria", secondary=proyecto_categoria_tabla, back_populates="proyectos"
    )
    paginas = relationship(
        "Pagina", back_populates="proyecto", cascade="all, delete-orphan"
    )


class ProyectoColaborador(Base):
    __tablename__ = "proyecto_colaboradores"

    proyecto_id = Column(Integer, ForeignKey("proyectos.id"), primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    rol = Column(
        SAEnum(RolColaborador), nullable=False, default=RolColaborador.VISUALIZADOR
    )

    proyecto = relationship("Proyecto", back_populates="colaboradores")
    usuario = relationship("Usuario", back_populates="proyectos_colaborados")
