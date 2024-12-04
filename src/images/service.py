from scipy import signal
import numpy as np

from images.models import ImageORM
from images import repository
from images.schemas import ImageIn, ImagesRange
from images.constants import IMAGE_SIZE


def resize_image(data: list[int]) -> list[int]:
    return signal.resample(data, IMAGE_SIZE).astype(np.uint8).tolist()


def apply_color_map(data: list[int]) -> list[int]:
    return data


async def create_image(image: ImageIn) -> ImageORM:
    image.data = resize_image(image.data)
    image = ImageORM(**image.model_dump())
    image = await repository.create_image(image)
    return image


async def get_image(image_id: int) -> ImageORM:
    image = await repository.get_image_by_id(image_id)
    image.data = apply_color_map(image.data)
    return image


async def delete_image(image_id: int) -> bool:
    return await repository.delete_image_by_id(image_id)


async def get_images(range: ImagesRange) -> list[ImageORM]:
    return await repository.get_images_range(range.min_depth, range.max_depth)
