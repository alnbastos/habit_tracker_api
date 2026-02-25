import pytest
from fastapi import status

from app.models.habit import Habit
from app.schemas.habit import HabitIn

from .conftest import client

URL = "/habits"


@pytest.fixture(scope="module")
async def habit():
    return await Habit.create(
        id=1,
        name="Matemática",
        description="Estudar para a prova de matemática",
        color="#F54927",
        frequency="daily",
        category="Estudo",
        is_archived=False,
    )


@pytest.fixture(scope="module")
def habit_in() -> dict:
    return HabitIn(
        name="Português",
        description="Estudar para a prova de português",
        color="#f5def8",
        frequency="daily",
        category="Estudo",
    ).model_dump()


@pytest.mark.anyio
class TestRead:
    def _assert_habit_json(self, returned_habit: dict, expected_habit: Habit):
        assert returned_habit["name"] == expected_habit.name
        assert returned_habit["description"] == expected_habit.description
        assert returned_habit["color"] == expected_habit.color
        assert returned_habit["frequency"] == expected_habit.frequency
        assert returned_habit["category"] == expected_habit.category
        assert returned_habit["is_archived"] is False

    async def test_read_habit(self, habit: Habit):
        # Act
        response = client.get(URL)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 1
        self._assert_habit_json(response.json()[0], habit)

    async def test_read_a_specific_habit(self, habit: Habit):
        # Arrange
        habit_id = 1
        url = URL + f"/{habit_id}"

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        self._assert_habit_json(response.json(), habit)

    async def test_read_a_specific_habit_not_exist(self, habit: Habit):
        # Arrange
        habit_id = 100
        url = URL + f"/{habit_id}"

        # Act
        response = client.get(url)

        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Habit not found."}


@pytest.mark.anyio
class TestCreate:
    @pytest.fixture(autouse=True)
    async def setup(self):
        # Limpa todos os hábitos antes de cada teste
        await Habit.all().delete()

    async def test_create_habit(self, habit_in: dict):
        # Act
        response = client.post(URL, json=habit_in)

        # Assert
        assert response.status_code == status.HTTP_201_CREATED

        habit_created = await Habit.get(name="Português")
        assert habit_created.description == habit_in["description"]
        assert habit_created.color == habit_in["color"]
        assert habit_created.is_archived is False

    async def test_create_habit_without_field_name(self, habit_in: dict):
        # Arrange
        habit_in.pop("name")

        # Act
        response = client.post(URL, json=habit_in)
        errors = response.json()["detail"]

        # Assert
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
        assert any(error["loc"] == ["body", "name"] for error in errors)
        assert len(await Habit.all()) == 0
