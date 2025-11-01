from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# Propiedades compartidas que todos los esquemas de Usuario tienen
class UsuarioBase(BaseModel):
    email: Optional[EmailStr] = None
    nombre_completo: Optional[str] = None
    esta_activo: Optional[bool] = True
    esta_verificado: Optional[bool] = False
    idioma: Optional[str] = "es"


# Propiedades para recibir en la creación de un usuario
class UsuarioCreate(UsuarioBase):
    contrasena: str


# Propiedades para recibir en la actualización de un usuario
class UsuarioUpdate(UsuarioBase):
    contrasena: Optional[str] = None


# Propiedades compartidas por los modelos en la base de datos
class UsuarioInDBBase(UsuarioBase):
    id: int
    ultimo_acceso: Optional[datetime] = None
    fecha_creacion: datetime

    model_config = {"from_attributes": True}


# Propiedades adicionales para devolver al cliente
class Usuario(UsuarioInDBBase):
    pass


# Propiedades adicionales almacenadas en la BD
class UsuarioInDB(UsuarioInDBBase):
    contrasena_hash: str
