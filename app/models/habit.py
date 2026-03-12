from enum import Enum

from tortoise import fields
from tortoise.models import Model


class Frequency(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    ANNUALLY = "annually"


class Habit(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=100)
    description = fields.TextField(null=True)
    color = fields.CharField(max_length=7)  # hexadecimal
    frequency = fields.CharEnumField(Frequency, max_length=10)
    category = fields.CharField(max_length=50)
    is_archived = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "habits"
