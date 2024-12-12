from typing import AsyncGenerator

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.pool import StaticPool

from src.database import DatabaseSessionManager


@pytest_asyncio.fixture()
async def session() -> AsyncGenerator[AsyncSession, None]:
    dns = "sqlite+aiosqlite:///:memory:"
    db = DatabaseSessionManager(dns, connect_args={"check_same_thread": False}, poolclass=StaticPool)
    await db.create_tables()
    async with db.sessionmaker() as session:
        yield session
    await db.close()
