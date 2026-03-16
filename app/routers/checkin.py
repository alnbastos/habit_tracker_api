from datetime import date

from fastapi import APIRouter, status

from app.schemas.checkin import CheckinIn, CheckinOut
from app.services.checkin import CheckinService

# from app.schemas.habit import HabitIn, HabitOut
from .habit import router as router_habit

router = APIRouter(prefix="/check-ins", tags=["Check-in"])
service = CheckinService()


@router_habit.get(
    "/{habit_id}/check-ins",
    summary="Listar check-ins de um hábito",
    status_code=status.HTTP_200_OK,
    response_model=list[CheckinOut],
)
async def read(
    habit_id: int, start_date: date | None = None, end_date: date | None = None
):
    return await service.read(habit_id, start_date, end_date)


@router_habit.post(
    "/{habit_id}/check-ins",
    summary="Registrar check-in",
    status_code=status.HTTP_201_CREATED,
    response_model=CheckinOut,
)
async def create(habit_id: int, checkin_in: CheckinIn):
    return await service.create(habit_id, checkin_in)


@router.delete(
    "/{checkin_id}",
    summary="Excluir check-in",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(checkin_id: int):
    return await service.delete(checkin_id)
