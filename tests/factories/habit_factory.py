from polyfactory.factories.pydantic_factory import ModelFactory
from app.schemas.habit import HabitIn


class HabitFactory(ModelFactory[HabitIn]):
    __model__ = HabitIn

    category = "Estudo"
    color = "#F54927"
    frequency = "daily"
    is_archived = False
