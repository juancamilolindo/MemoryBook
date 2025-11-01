from api.dependencies import get_current_active_user, get_db
from fastapi import APIRouter, Depends, HTTPException
from models.usuario import Usuario
from schemas import Proyecto, ProyectoCreate, ProyectoUpdate
from services import proyecto as proyecto_service
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Proyecto)
def create_proyecto(
    *,
    db: Session = Depends(get_db),
    proyecto_in: ProyectoCreate,
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Crea un nuevo proyecto.
    """
    if not current_user:
        raise HTTPException(status_code=403, detail="Not authorized")

    proyecto = proyecto_service.create_proyecto(
        db=db,
        proyecto_in=proyecto_in,
        usuario_id=current_user.id,  # type: ignore
    )
    return proyecto


@router.get("/{proyecto_id}", response_model=Proyecto)
def get_proyecto(
    *,
    db: Session = Depends(get_db),
    proyecto_id: int,
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Obtiene un proyecto por su ID.
    """
    proyecto = proyecto_service.get_proyecto(db=db, proyecto_id=proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto


@router.put("/{proyecto_id}", response_model=Proyecto)
def update_proyecto(
    *,
    db: Session = Depends(get_db),
    proyecto_id: int,
    proyecto_in: ProyectoUpdate,
    current_user: Usuario = Depends(get_current_active_user),
):
    """
    Actualiza un proyecto existente.
    """
    proyecto = proyecto_service.get_proyecto(db=db, proyecto_id=proyecto_id)
    if not proyecto or proyecto.usuario_id != current_user.id:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    proyecto = proyecto_service.update_proyecto(
        db=db, db_obj=proyecto, obj_in=proyecto_in
    )
    return proyecto
