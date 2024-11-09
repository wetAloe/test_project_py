import fastapi
from pydantic import BaseModel


class Image(BaseModel):
    data: list[int]


app = fastapi.FastAPI()

@app.post("/upload_image")
async def upload_image(image: Image):
    if len(image.data) == 0:
        return {"error": "No image data provided"}

    return {"message": "Image uploaded", "length": len(image.data)}
