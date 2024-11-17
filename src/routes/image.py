from fastapi import APIRouter

from dependencies import SessionDep
from models.image import Image
from repositories.image import ImageRepository

image_router = APIRouter()


@image_router.post("/images/")
async def upload_image(image: Image, session: SessionDep):
    if len(image.data) == 0:
        return {"error": "No image data provided"}

    _ = await ImageRepository.upload_image(session, image)
    return {"message": "Image uploaded", "length": len(image.data)}
