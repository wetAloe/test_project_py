from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_db_and_tables
from images.routes import router as image_router


def create_app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        await create_db_and_tables()
        yield

    app = FastAPI(lifespan=lifespan)
    app.include_router(image_router)
    return app
