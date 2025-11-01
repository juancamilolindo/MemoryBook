from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from .elemento_pagina import ElementoPagina, ElementoPaginaCreate


# Esquemas para Páginas
class PaginaBase(BaseModel):
    numero_pagina: int
    plantilla_origen_id: Optional[int] = None


class PaginaCreate(PaginaBase):
    elementos: List[ElementoPaginaCreate] = []


class Pagina(PaginaBase):
    id: int
    proyecto_id: int
    elementos: List[ElementoPagina] = []

    model_config = ConfigDict(from_attributes=True)
