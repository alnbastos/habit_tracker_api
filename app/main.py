from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from .exceptions import NotFoundError
from .configs.database import lifespan
from .routers.habit import router as router_habit

app = FastAPI(title="Habit Tracker API", lifespan=lifespan)

app.include_router(router_habit)


@app.exception_handler(NotFoundError)
async def not_found_error_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc) + " not found."},
    )
