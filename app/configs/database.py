from tortoise import Tortoise
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI.

    Initializes the Tortoise ORM connection on startup and
    closes all connections on shutdown.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    await Tortoise.init(
        db_url=settings.database_url,
        modules={"models": ["app.models"]},
        timezone="UTC",
        use_tz=True,
    )

    yield

    await Tortoise.close_connections()


# Tortoise ORM configuration used by Aerich for migrations.
# - 'connections': defines the database URLs
# - 'apps': lists the models to be managed and their default connection
TORTOISE_ORM = {
    "connections": {
        "default": settings.database_url,
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
