from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .configs.database import lifespan
from .exceptions.base import AppError
from .routers.checkin import router as router_checkin
from .routers.habit import router as router_habit

app = FastAPI(title="Habit Tracker API", lifespan=lifespan)

app.include_router(router_habit)
app.include_router(router_checkin)


@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
