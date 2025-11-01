from fastapi import APIRouter

from .endpoints import proyectos

api_router = APIRouter()

# Configuración de routers a incluir en el router maestro
ROUTERS_CONFIG = [
    (
        proyectos.router,
        "/proyectos",
        [
            "Proyectos",
        ],
    ),
    # Aquí añadiremos futuros routers (usuarios, plantillas, etc.)
]

for router, prefix, tags in ROUTERS_CONFIG:
    api_router.include_router(router, prefix=prefix, tags=tags)  # type: ignore
