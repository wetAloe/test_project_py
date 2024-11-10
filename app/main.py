import os

import fastapi
from pydantic import BaseModel
from sqlalchemy import create_engine

from models import images_table


engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
app = fastapi.FastAPI()

class Image(BaseModel):
    data: list[int]

@app.post("/upload_image")
async def upload_image(image: Image):
    if len(image.data) == 0:
        return {"error": "No image data provided"}

    with engine.connect() as conn:
        conn.execute(images_table.insert(), [{"data": image.data}])
        conn.commit()

    return {"message": "Image uploaded", "length": len(image.data)}
