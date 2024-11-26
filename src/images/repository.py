from sqlmodel.ext.asyncio.session import AsyncSession

from images.models import Image


class ImageRepository:
    @staticmethod
    async def upload_image(session: AsyncSession, image: Image) -> Image:
        session.add(image)
        await session.commit()
        await session.refresh(image)
        return image

    @staticmethod
    async def get_image(session: AsyncSession, image_id: int) -> Image:
        image = await session.get(Image, image_id)
        return image

    @staticmethod
    async def delete_image(session: AsyncSession, image_id: int) -> None:
        image = await session.get(Image, image_id)
        if image:
            await session.delete(image)
            await session.commit()

    @staticmethod
    async def update_image(session: AsyncSession, image_id: int, image: Image) -> Image:
        db_image = await session.get(Image, image_id)
        if not db_image:
            raise ValueError(f"Image with id {image_id} not found")
        db_image.data = image.data
        await session.commit()
        await session.refresh(db_image)
        return db_image
