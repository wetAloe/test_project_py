from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from settings import get_database_settings

_settings = get_database_settings()
_async_engine = create_async_engine(_settings.dns)
SessionLocal = async_sessionmaker(_async_engine)


class Base(DeclarativeBase):
    pass


async def create_db_and_tables() -> None:
    async with _async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
