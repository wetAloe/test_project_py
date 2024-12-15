from typing import AsyncGenerator
import asyncio

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.app import create_app
from src.database import DatabaseSessionManager, get_session


@pytest.fixture()
def client(database: DatabaseSessionManager) -> TestClient:
    asyncio.run(database.drop_create_tables())
    async def override_get_session() -> AsyncGenerator[AsyncSession, None]:
        async with database.sessionmaker() as session:
            yield session

    app = create_app()
    app.dependency_overrides[get_session] = override_get_session
    return TestClient(app)
