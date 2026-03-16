import datetime as dt

from pydantic import BaseModel, field_validator

from app.exceptions.checkin import FutureCheckinDateError


class CheckinBase(BaseModel):
    notes: str | None = None
    date: dt.date


class CheckinIn(CheckinBase):
    @field_validator("date")
    @classmethod
    def validate_date(cls, value: dt.date):
        if value > dt.date.today():
            raise FutureCheckinDateError()
        return value


class CheckinOut(CheckinBase):
    id: int
    habit_id: int
    created_at: dt.datetime
