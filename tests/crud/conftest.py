from typing import AsyncGenerator

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import DatabaseSessionManager


@pytest_asyncio.fixture()
async def session(database: DatabaseSessionManager) -> AsyncGenerator[AsyncSession, None]:
    await database.drop_create_tables()
    async with database.sessionmaker() as session:
        yield session