from typing import Annotated

from fastapi import APIRouter, Depends

from dependecies import SessionDep
from images.schemas import ImageIn, ImageOut, ImagesRange
from images import service, repository
from images.models import ImageORM

router = APIRouter()


@router.post("/images/", response_model=ImageOut)
async def upload_image(image: ImageIn, session: SessionDep):
    image.data = service.resize_image(image.data)
    image = await repository.create_image(session, ImageORM(**image.model_dump()))
    return image


@router.delete("/images/{image_id}")
async def delete_image(image_id: int, session: SessionDep):
    await repository.delete_image_by_id(session, image_id)


@router.get("/images/{image_id}", response_model=ImageOut)
async def get_image(image_id: int, session: SessionDep):
    image = await repository.get_image_by_id(session, image_id)
    image.data = service.apply_color_map(image.data)
    return image


@router.get("/images/", response_model=list[ImageOut])
async def get_images(range: Annotated[ImagesRange, Depends()], session: SessionDep):
    images = await repository.get_images_range(session, range.min_depth, range.max_depth)
    return images
