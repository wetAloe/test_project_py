import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.images.crud import create_image, get_image_by_id, delete_image_by_id, get_images_range
from src.images.models import ImageORM
from src.exceptions import EntityDoesNotExistException


@pytest.fixture
def test_image() -> ImageORM:
    return ImageORM(data=bytes([0] * 200))


@pytest.mark.asyncio
async def test_image_create(session: AsyncSession, test_image: ImageORM):
    test_image = await create_image(session, test_image)
    assert test_image.id is not None


@pytest.mark.asyncio
async def test_image_get_by_id(session: AsyncSession, test_image: ImageORM):
    test_image = await create_image(session, test_image)
    image = await get_image_by_id(session, test_image.id)
    assert image is not None
    assert image.id == test_image.id
    assert image.data == test_image.data


@pytest.mark.asyncio
async def test_image_delete_by_id(session: AsyncSession, test_image: ImageORM):
    test_image = await create_image(session, test_image)
    image = await delete_image_by_id(session, test_image.id)
    assert image is not None
    assert image.id == test_image.id
    assert image.data == test_image.data
    with pytest.raises(EntityDoesNotExistException):
        await get_image_by_id(session, image.id)


@pytest.mark.asyncio
async def test_image_get_range(session: AsyncSession, test_image: ImageORM):
    test_image = await create_image(session, test_image)
    images = await get_images_range(session, 1, 100)
    assert len(images) == 1
    assert images[0].id == test_image.id
    assert images[0].data == test_image.data
