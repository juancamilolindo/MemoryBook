from typing import Any

from models.pagina import TipoElemento
from pydantic import BaseModel, ConfigDict


# Esquemas para Elementos de Página
class ElementoPaginaBase(BaseModel):
    tipo_elemento: TipoElemento
    posicion_x: float = 0
    posicion_y: float = 0
    ancho: float = 100
    alto: float = 100
    rotacion: float = 0
    orden_capa: int = 0
    contenido: Any  # JSONB puede contener cualquier cosa


class ElementoPaginaCreate(ElementoPaginaBase):
    pass


class ElementoPagina(ElementoPaginaBase):
    id: int
    pagina_id: int

    model_config = ConfigDict(from_attributes=True)
