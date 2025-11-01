from models.pagina import ElementoPagina, Pagina
from models.proyecto import Proyecto
from schemas import ProyectoCreate, ProyectoUpdate
from sqlalchemy.orm import Session


def get_proyecto(db: Session, proyecto_id: int):
    return db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()


def update_proyecto(
    db: Session, *, db_obj: Proyecto, obj_in: ProyectoUpdate
) -> Proyecto:
    obj_data = db_obj.model_dump()
    update_data = obj_in.model_dump(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_proyecto(
    db: Session, *, proyecto_in: ProyectoCreate, usuario_id: int
) -> Proyecto:
    # Excluye las páginas del diccionario principal para crear el proyecto primero
    proyecto_data = proyecto_in.model_dump(exclude={"paginas"})
    db_proyecto = Proyecto(**proyecto_data, usuario_creacion_id=usuario_id)

    db.add(db_proyecto)
    db.flush()  # Para obtener el ID del proyecto para las relaciones

    for pagina_in in proyecto_in.paginas:
        pagina_data = pagina_in.model_dump(exclude={"elementos"})
        db_pagina = Pagina(
            **pagina_data, proyecto_id=db_proyecto.id, usuario_creacion_id=usuario_id
        )
        db.add(db_pagina)
        db.flush()  # Para obtener el ID de la página para los elementos

        for elemento_in in pagina_in.elementos:
            db_elemento = ElementoPagina(
                **elemento_in.model_dump(),
                pagina_id=db_pagina.id,
                usuario_creacion_id=usuario_id,
            )
            db.add(db_elemento)

    db.commit()
    db.refresh(db_proyecto)
    return db_proyecto
