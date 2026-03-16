from tortoise import fields
from tortoise.models import Model


class Checkin(Model):
    id = fields.IntField(primary_key=True)
    habit = fields.ForeignKeyField(
        "models.Habit",
        related_name="checkins",
        on_delete=fields.CASCADE,
    )
    date = fields.DateField()
    notes = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "checkins"
        unique_together = (("habit_id", "date"),)
