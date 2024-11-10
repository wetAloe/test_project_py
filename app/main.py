import os

import fastapi
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import create_async_engine

from models import images_table


engine = create_async_engine(os.getenv("DATABASE_URL"))
app = fastapi.FastAPI()

class Image(BaseModel):
    data: list[int]

@app.post("/upload_image")
async def upload_image(image: Image):
    if len(image.data) == 0:
        return {"error": "No image data provided"}

    async with engine.connect() as conn:
        await conn.execute(images_table.insert(), [{"data": image.data}])
        await conn.commit()

    return {"message": "Image uploaded", "length": len(image.data)}
