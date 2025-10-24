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

    @app.get("/", tags=["Status"])
    def read_root():
        return {"message": "Welcome to the MemoryBook API"}

    @app.get("/health", tags=["Status"])
    def health_check():
        return {"status": "ok"}

    return app


app = create_app()
