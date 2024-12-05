from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from images.models import ImageORM
from exceptions import EntityDoesNotExistException


async def create_image(session: AsyncSession, image: ImageORM) -> ImageORM:
    session.add(image)
    await session.commit()
    await session.refresh(image)
    return image


async def get_image_by_id(session: AsyncSession, image_id: int) -> ImageORM:
    image = await session.get(ImageORM, image_id)
    if not image:
        raise EntityDoesNotExistException
    return image


async def delete_image_by_id(session: AsyncSession, image_id: int) -> ImageORM:
    image = await get_image_by_id(session, image_id)
    await session.delete(image)
    await session.commit()
    return image


async def get_images_range(session: AsyncSession, min_depth: int, max_depth: int) -> list[ImageORM]:
    images = await session.execute(
        select(ImageORM)
            .where(ImageORM.id.between(min_depth, max_depth))
    )
    return images.scalars().all()
