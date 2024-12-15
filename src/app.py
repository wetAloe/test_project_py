from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import DatabaseSessionManager
from src.settings import DatabaseSettings
from src.images.routes import router as image_router


def create_app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.db = DatabaseSessionManager(DatabaseSettings().dns)
        await app.state.db.drop_create_tables()
        yield
        await app.state.db.close()

    app = FastAPI(lifespan=lifespan)
    app.include_router(image_router)
    return app
