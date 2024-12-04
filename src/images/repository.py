from sqlalchemy import select

from images.models import ImageORM
from database import SessionLocal


async def create_image(image: ImageORM) -> ImageORM:
    async with SessionLocal() as session:
        session.add(image)
        await session.commit()
        await session.refresh(image)
    return image


async def get_image_by_id(image_id: int) -> ImageORM:
    async with SessionLocal() as session:
        image = await session.get(ImageORM, image_id)
    return image


async def delete_image_by_id(image_id: int) -> bool:
    async with SessionLocal() as session:
        image = await session.get(ImageORM, image_id)
        if image:
            session.delete(image)
            await session.commit()
            return True
        return False


async def get_images_range(min_depth: int, max_depth: int) -> list[ImageORM]:
    async with SessionLocal() as session:
        images = await session.execute(
            select(ImageORM)
                .where(ImageORM.id.between(min_depth, max_depth))
        )
        return images.scalars().all()
