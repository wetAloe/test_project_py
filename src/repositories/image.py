from sqlmodel.ext.asyncio.session import AsyncSession

from models.image import Image


class ImageRepository:
    @staticmethod
    async def upload_image(session: AsyncSession, image: Image):
        session.add(image)
        await session.commit()
        await session.refresh(image)
        return image
