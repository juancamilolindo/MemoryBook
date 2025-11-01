import models
import schemas
import services
from api.dependencies import get_current_active_user, get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=schemas.Proyecto)
def create_proyecto(
    *,
    db: Session = Depends(get_db),
    proyecto_in: schemas.ProyectoCreate,
    current_user: models.Usuario = Depends(get_current_active_user),
):
    """
    Crea un nuevo proyecto.
    """
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")

    proyecto = services.proyecto.create_proyecto(
        db=db,
        proyecto_in=proyecto_in,
        usuario_id=current_user.id,  # type: ignore
    )
    return proyecto


@router.get("/{proyecto_id}", response_model=schemas.Proyecto)
def get_proyecto(
    *,
    db: Session = Depends(get_db),
    proyecto_id: int,
    current_user: models.Usuario = Depends(get_current_active_user),
):
    """
    Obtiene un proyecto por su ID.
    """
    proyecto = services.proyecto.get_proyecto(db=db, proyecto_id=proyecto_id)
    if not proyecto or proyecto.usuario_id != current_user.id:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto


@router.put("/{proyecto_id}", response_model=schemas.Proyecto)
def update_proyecto(
    *,
    db: Session = Depends(get_db),
    proyecto_id: int,
    proyecto_in: schemas.ProyectoUpdate,
    current_user: models.Usuario = Depends(get_current_active_user),
):
    """
    Actualiza un proyecto existente.
    """
    proyecto = services.proyecto.get_proyecto(db=db, proyecto_id=proyecto_id)
    if not proyecto or proyecto.usuario_id != current_user.id:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    proyecto = services.proyecto.update_proyecto(
        db=db, db_obj=proyecto, obj_in=proyecto_in
    )
    return proyecto
