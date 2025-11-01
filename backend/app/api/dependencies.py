from typing import Generator

import crud
import models
from db.session import SessionLocal
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db)) -> models.Usuario:
    """
    Dependency for development to bypass authentication.
    Returns the first active user found in the database by using the CRUD layer.
    """
    user = crud.usuario.get_first_active_user(db)
    if not user:
        raise HTTPException(
            status_code=404,
            detail=(
                "Dev auth bypass failed: No active users found in DB. "
                "Please create an active user to proceed."
            ),
        )
    return user


def get_current_active_user(
    current_user: models.Usuario = Depends(get_current_user),
) -> models.Usuario:
    """
    Dependency to get the current active user.
    It checks if the user is active using the CRUD layer.
    """
    if not crud.usuario.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def require_role(required_role: str):
    """
    Dependency factory to require a specific role.
    NOTE: The 'Usuario' model does not currently have a 'rol' attribute.
    This will need to be added for this dependency to work correctly.
    """

    def role_checker(
        current_user: models.Usuario = Depends(get_current_active_user),
    ) -> models.Usuario:
        if (
            not hasattr(current_user, "rol")
            or getattr(current_user, "rol") != required_role
        ):
            raise HTTPException(
                status_code=403,
                detail=f"Action requires '{required_role}' role.",
            )
        return current_user

    return role_checker
