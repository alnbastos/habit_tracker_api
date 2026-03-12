import pytest
from fastapi.testclient import TestClient
from tortoise import Tortoise

from app.main import app

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
async def init_db():
    await Tortoise.init(
        db_url="sqlite://:memory:",
        modules={"models": ["app.models.habit"]}
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()
