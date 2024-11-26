from sqlmodel.ext.asyncio.session import AsyncSession

from images.models import Image
from images.repository import ImageRepository


async def upload_image(session: AsyncSession, image: Image) -> Image:
    return await ImageRepository.upload_image(session, image)


