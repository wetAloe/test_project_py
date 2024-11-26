from scipy import signal
import numpy as np
from sqlmodel.ext.asyncio.session import AsyncSession

from images.models import Image
from images.repository import ImageRepository


def resize_image(image: Image) -> Image:
    image.data = signal.resample(image.data, 150).astype(np.uint8)
    return image


def apply_color_map(image: Image) -> Image:
    return image


class ImageService:
    @staticmethod
    async def upload_image(session: AsyncSession, image: Image) -> Image | dict:
        image = resize_image(image)
        return await ImageRepository.upload_image(session, image)

    @staticmethod
    async def get_image(session: AsyncSession, image_id: int) -> Image:
        image = await ImageRepository.get_image(session, image_id)
        return apply_color_map(image)

    @staticmethod
    async def delete_image(session: AsyncSession, image_id: int) -> None:
        return await ImageRepository.delete_image(session, image_id)

    @staticmethod
    async def update_image(session: AsyncSession, image_id: int, image: Image) -> None:
        image = resize_image(image)
        return await ImageRepository.update_image(session, image_id, image)
