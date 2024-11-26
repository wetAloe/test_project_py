from fastapi import APIRouter

from dependencies import SessionDep
from images.models import Image
from images.service import ImageService

router = APIRouter()


@router.post("/images/")
async def upload_image(image: Image, session: SessionDep):
    image = await ImageService.upload_image(session, image)
    return image


@router.get("/images/{image_id}")
async def get_image(image_id: int, session: SessionDep):
    image = await ImageService.get_image(session, image_id)
    return image


@router.delete("/images/{image_id}")
async def delete_image(image_id: int, session: SessionDep):
    await ImageService.delete_image(session, image_id)
    return {"message": "Image deleted"}


@router.put("/images/{image_id}")
async def update_image(image_id: int, image: Image, session: SessionDep):
    await ImageService.update_image(session, image_id, image)
    return image
