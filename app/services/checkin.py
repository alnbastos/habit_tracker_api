from datetime import date

from tortoise.exceptions import IntegrityError

from app.exceptions.base import AlreadyExistsError, NotFoundError
from app.models.checkin import Checkin
from app.models.habit import Habit
from app.schemas.checkin import CheckinIn, CheckinOut


class CheckinService:
    async def read(
        self, habit_id: int, start_date: date | None, end_date: date | None
    ) -> list[CheckinOut]:
        filters = {"habit_id": habit_id}

        if start_date:
            filters["date__gte"] = start_date

        if end_date:
            filters["date__lte"] = end_date

        return await Checkin.filter(**filters)

    async def create(self, habit_id: int, checkin_in: CheckinIn) -> CheckinOut:
        habit_exists = await Habit.filter(id=habit_id).exists()

        if not habit_exists:
            raise NotFoundError("Habit")

        try:
            checkin = await Checkin.create(
                habit_id=habit_id,
                **checkin_in.model_dump(exclude_none=True),
            )
        except IntegrityError:
            raise AlreadyExistsError("Checkin")

        return CheckinOut.model_validate(checkin)

    async def delete(self, delete: int):
        checkin = await Checkin.filter(id=delete).delete()

        if checkin == 0:
            raise NotFoundError("Checkin")

        return {"detail": "Checkin successfully deleted."}
