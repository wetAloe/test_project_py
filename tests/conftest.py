import pytest
from sqlalchemy.pool import StaticPool

from src.database import DatabaseSessionManager


@pytest.fixture(scope="package")
def database() -> DatabaseSessionManager:
    dns = "sqlite+aiosqlite:///:memory:"
    return DatabaseSessionManager(dns, connect_args={"check_same_thread": False}, poolclass=StaticPool)
