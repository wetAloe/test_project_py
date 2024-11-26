from fastapi import APIRouter

from dependencies import SessionDep
from images.models import Image
from images.repository import ImageRepository

router = APIRouter()


@router.post("/images/")
async def upload_image(image: Image, session: SessionDep):
    if len(image.data) == 0:
        return {"error": "No image data provided"}

    _ = await ImageRepository.upload_image(session, image)
    return {"message": "Image uploaded", "length": len(image.data)}


@router.get("/images/{image_id}")
async def get_image(image_id: str, session: SessionDep):
    image = await ImageRepository.get_image(session, image_id)
    return image


@router.delete("/images/{image_id}")
async def delete_image(image_id: str, session: SessionDep):
    await ImageRepository.delete_image(session, image_id)
    return {"message": "Image deleted"}


@router.put("/images/{image_id}")
async def update_image(image_id: str, image: Image, session: SessionDep):
    await ImageRepository.update_image(session, image_id, image)
    return {"message": "Image updated"}
