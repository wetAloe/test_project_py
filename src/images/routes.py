from typing import Annotated

from fastapi import APIRouter, Depends

from src.dependecies import SessionDep
from src.images.schemas import ImageIn, ImageOut, ImagesRange
from src.images import service
from src.images.models import ImageORM
from src.images import crud

router = APIRouter()


@router.post("/images/", response_model=ImageOut)
async def upload_image(image: ImageIn, session: SessionDep):
    image.data = service.resize_image(image.data)
    image = await crud.create_image(session, ImageORM(**image.model_dump()))
    return image


@router.delete("/images/{image_id}")
async def delete_image(image_id: int, session: SessionDep):
    await crud.delete_image_by_id(session, image_id)


@router.get("/images/{image_id}", response_model=ImageOut)
async def get_image(image_id: int, session: SessionDep):
    image = await crud.get_image_by_id(session, image_id)
    image.data = service.apply_color_map(image.data)
    return image


@router.get("/images/", response_model=list[ImageOut])
async def get_images(range: Annotated[ImagesRange, Depends()], session: SessionDep):
    images = await crud.get_images_range(session, range.min_depth, range.max_depth)
    return images
