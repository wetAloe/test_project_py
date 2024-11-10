import os
from contextlib import asynccontextmanager

import fastapi
from pydantic import BaseModel
from queries import create_tables
from sqlalchemy import create_engine


engine = create_engine(os.getenv("DATABASE_URL"), echo=True)

@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    with engine.connect() as conn:
        create_tables(engine)
        conn.commit()
    yield

app = fastapi.FastAPI(lifespan=lifespan)

class Image(BaseModel):
    data: list[int]

@app.post("/upload_image")
async def upload_image(image: Image):
    if len(image.data) == 0:
        return {"error": "No image data provided"}

    return {"message": "Image uploaded", "length": len(image.data)}
