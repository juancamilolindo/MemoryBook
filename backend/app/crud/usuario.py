from typing import Any, Optional

from models.usuario import Usuario
from sqlalchemy.orm import Session


def get(self, db: Session, id: Any) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.id == id).first()


def get_by_email(self, db: Session, *, email: str) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.email == email).first()


def is_active(self, user: Usuario) -> bool:
    return user.esta_activo  # type: ignore


def get_first_active_user(self, db: Session) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.esta_activo).first()
