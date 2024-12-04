from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends

from images.schemas import ImageIn, ImageOut, ImagesRange
from images import service

router = APIRouter()


@router.post("/images/", response_model=ImageOut)
async def upload_image(image: ImageIn):
    image = await service.create_image(image)
    return image


@router.delete("/images/{image_id}")
async def delete_image(image_id: int):
    await service.delete_image(image_id)
    return {"message": "Image deleted"}


@router.get("/images/{image_id}", response_model=ImageOut)
async def get_image(image_id: int):
    image = await service.get_image(image_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image


@router.get("/images/", response_model=list[ImageOut])
async def get_images(range: Annotated[ImagesRange, Depends()]):
    images = await service.get_images(range)
    return images
