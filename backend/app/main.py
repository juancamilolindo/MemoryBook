from api.api import api_router  # Importamos el router maestro
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    """
    App factory for creating the FastAPI app.
    """
    app = FastAPI(title="MemoryBook API")

    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins for now
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Incluimos el router maestro de la API
    app.include_router(
        api_router,
        # Aquí podríamos añadir dependencias globales para toda la API
        # dependencies=[Depends(deps.get_current_active_user)]
    )

    @app.get("/", tags=["Status"])
    def read_root():
        return {"message": "Welcome to the MemoryBook API"}

    @app.get("/health", tags=["Status"])
    def health_check():
        return {"status": "ok"}

    return app


app = create_app()
