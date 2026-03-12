import pytest
from fastapi import status
from datetime import timezone

from app.models.habit import Habit
from app.schemas.habit import HabitIn
from .factories.habit_factory import HabitFactory

from .conftest import client

URL = "/habits"


@pytest.fixture(scope="function")
async def habit() -> Habit:
    """Cria um hábito no banco usando factory."""
    payload = HabitFactory.build()
    return await Habit.create(**payload.model_dump())


@pytest.fixture(scope="function")
def habit_in() -> HabitIn:
    """Factory de payload para criação de hábito via API."""
    return HabitFactory.build(
        name="Matemática",
        description="Estudar para a prova de matemática",
    )


def habit_to_dict(habit: Habit, include_id=False):
    data = {
        "name": habit.name,
        "description": habit.description,
        "color": habit.color,
        "frequency": habit.frequency,
        "category": habit.category,
        "is_archived": habit.is_archived,
    }
    if include_id:
        data.update({
            "id": habit.id,
            "created_at": habit.created_at.astimezone(timezone.utc)
            .isoformat(timespec='microseconds')
            .replace("+00:00", "Z"),
            "updated_at": habit.updated_at.astimezone(timezone.utc)
            .isoformat(timespec='microseconds')
            .replace("+00:00", "Z"),
        })
    return data


@pytest.mark.anyio
class TestRead:
    async def test_read_habit(self, habit: Habit):
        # Act
        response = client.get(URL)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 1
        assert response.json()[0] == habit_to_dict(habit, True)

    async def test_read_a_specific_habit(self, habit: Habit):
        # Arrange
        url = URL + f"/{habit.id}"

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == habit_to_dict(habit, True)


@pytest.mark.anyio
class TestCreate:
    @pytest.fixture(autouse=True)
    async def setup(self):
        # Limpa todos os hábitos antes de cada teste
        await Habit.all().delete()

    async def test_create_habit(self, habit_in: HabitIn):
        # Act
        response = client.post(URL, json=habit_in.model_dump())

        # Assert
        assert response.status_code == status.HTTP_201_CREATED

        habit_created = await Habit.get(name=habit_in.name)
        assert habit_to_dict(habit_created) == habit_in.model_dump()

    async def test_create_habit_missing_name(self, habit_in: HabitIn):
        # Arrange
        data = habit_in.model_dump()
        data.pop("name")

        # Act
        response = client.post(URL, json=data)
        errors = response.json()["detail"]

        # Assert
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
        assert any(error["loc"] == ["body", "name"] for error in errors)
        assert len(await Habit.all()) == 0


@pytest.mark.anyio
class TestUpdate:
    async def test_update_habit(self, habit: Habit):
        # Arrange
        url = URL + f"/{habit.id}"
        payload = HabitFactory.build()

        # Act
        response = client.put(url, json=payload.model_dump())

        # Assert
        assert response.status_code == status.HTTP_200_OK

        # Valida se os dados foram realmente atualizados no DB
        habit_db = await Habit.get(id=habit.id)
        assert habit_to_dict(habit_db) == payload.model_dump()

    async def test_archive_habit(self, habit: Habit):
        # Arrange
        url = URL + f"/{habit.id}/archive"

        # Act
        response = client.patch(url)

        # Assert
        assert response.status_code == status.HTTP_200_OK

        # Valida se os dados foram realmente atualizados no DB
        habit_db = await Habit.get(id=habit.id)
        assert habit_db.is_archived is True


@pytest.mark.anyio
class TestDelete:
    async def test_delete_habit(self, habit: Habit):
        # Arrange
        url = URL + f"/{habit.id}"

        # Act
        response = client.delete(url)

        # Assert
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert await Habit.filter(id=habit.id) == []


@pytest.mark.anyio
class TestNonExistingHabit:
    HABIT_ID = 9999
    URL = URL + f"/{HABIT_ID}"

    def _assert_not_found(self, response):
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Habit not found."}

    async def test_read(self):
        response = client.get(self.URL)
        self._assert_not_found(response)

    async def test_update(self):
        payload = HabitFactory.build()
        response = client.put(self.URL, json=payload.model_dump())
        self._assert_not_found(response)

    async def test_archive(self):
        url = self.URL + "/archive"
        response = client.patch(url)
        self._assert_not_found(response)

    async def test_delete(self):
        response = client.delete(self.URL)
        self._assert_not_found(response)
