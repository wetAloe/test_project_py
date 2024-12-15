from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine
from sqlalchemy.orm import DeclarativeBase
from fastapi import Request


class Base(DeclarativeBase):
    pass


class DatabaseSessionManager:
    def __init__(self, dns: str, **kwargs):
        self._async_engine: AsyncEngine | None = create_async_engine(dns, **kwargs)
        self.sessionmaker: async_sessionmaker[AsyncSession] = async_sessionmaker(self._async_engine, class_=AsyncSession)

    async def close(self):
        await self._async_engine.dispose()

    async def drop_create_tables(self):
        async with self._async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


async def get_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    async with request.app.state.db.sessionmaker() as session:
        yield session
