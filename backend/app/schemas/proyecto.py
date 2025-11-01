from typing import List, Optional

from models.proyecto import EstadoProyecto, TipoProyecto, VisibilidadProyecto
from pydantic import BaseModel, ConfigDict

from .pagina import Pagina, PaginaCreate


# Esquemas para Proyectos
class ProyectoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    tipo_proyecto: TipoProyecto
    url_imagen_portada: Optional[str] = None
    visibilidad: VisibilidadProyecto = VisibilidadProyecto.PRIVADO
    estado: EstadoProyecto = EstadoProyecto.ACTIVO


class ProyectoCreate(ProyectoBase):
    paginas: List[PaginaCreate] = []


class Proyecto(ProyectoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    usuario_creacion_id: int
    paginas: List[Pagina] = []


class ProyectoUpdate(ProyectoBase):
    nombre: Optional[str] = None
    tipo_proyecto: Optional[TipoProyecto] = None
    visibilidad: Optional[VisibilidadProyecto] = None
    estado: Optional[EstadoProyecto] = None
