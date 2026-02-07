from tortoise.exceptions import DoesNotExist

from app.exceptions import NotFoundError
from app.models.habit import Habit
from app.schemas.habit import HabitIn, HabitOut


class HabitService:
    async def read(
        self,
        is_archived: bool | None,
        category: str | None,
    ) -> list[HabitOut]:
        habits = Habit.all()

        if is_archived is not None:
            habits = habits.filter(is_archived=is_archived)
        if category:
            habits = habits.filter(category=category)

        return await habits

    async def detail(self, habit_id: int) -> HabitOut:
        try:
            return await Habit.get(id=habit_id)
        except DoesNotExist:
            raise NotFoundError("Habit")

    async def create(self, habit_in: HabitIn) -> HabitOut:
        return await Habit.create(**habit_in.model_dump())

    async def update(self, habit_id: int, habit_in: HabitIn) -> HabitOut:
        habit = await Habit.get_or_none(id=habit_id)

        if habit is None:
            raise NotFoundError("Habit")

        habit.update_from_dict(habit_in.model_dump())
        await habit.save()

        return habit

    async def delete(self, habit_id: int):
        deleted_count = await Habit.filter(id=habit_id).delete()

        if deleted_count == 0:
            raise NotFoundError("Habit")

        return {"detail": "Habit successfully deleted."}
