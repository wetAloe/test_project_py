from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from settings import get_database_settings


_settings = get_database_settings()
_async_engine = create_async_engine(_settings.dns)


async def create_db_and_tables():
    async with _async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    async_session = sessionmaker(
       bind=_async_engine, class_=AsyncSession, expire_on_commit=False
   )
    async with async_session() as session:
        yield session
