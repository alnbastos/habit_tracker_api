from datetime import datetime

from pydantic import BaseModel


class HabitBase(BaseModel):
    name: str
    description: str | None = None
    color: str
    frequency: str
    category: str
    is_archived: bool = False


class HabitIn(HabitBase):
    pass


class HabitOut(HabitBase):
    id: int
    created_at: datetime
    updated_at: datetime
