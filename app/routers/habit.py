from fastapi import APIRouter, status

from app.schemas.habit import HabitIn, HabitOut
from app.services.habit import HabitService

router = APIRouter(prefix="/habits", tags=["Habits"])
service = HabitService()


@router.get(
    "/",
    summary="Listar todos os hábitos cadastrados",
    status_code=status.HTTP_200_OK,
    response_model=list[HabitOut],
)
async def read(is_archived: bool | None = None, category: str | None = None):
    return await service.read(is_archived, category)


@router.get(
    "/{habit_id}",
    summary="Visualizar detalhes de um hábito específico",
    status_code=status.HTTP_200_OK,
    response_model=HabitOut,
)
async def details(habit_id: int):
    return await service.detail(habit_id)


@router.post(
    "/",
    summary="Criar um novo hábito com nome, descrição, " "cor e frequência desejada",
    status_code=status.HTTP_201_CREATED,
    response_model=HabitOut,
)
async def create(habit_in: HabitIn):
    return await service.create(habit_in)


@router.put(
    "/{habit_id}",
    summary="Atualizar informações de um hábito",
    status_code=status.HTTP_200_OK,
    response_model=HabitOut,
)
async def update(habit_id: int, habit_in: HabitIn):
    return await service.update(habit_id, habit_in)


@router.delete(
    "/{habit_id}",
    summary="Excluir um hábito (e seus check-ins associados)",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(habit_id: int):
    return await service.delete(habit_id)


@router.patch(
    "/{habit_id}/archive",
    summary="Arquivar/desarquivar hábito",
    status_code=status.HTTP_200_OK,
    response_model=HabitOut,
)
async def archive(habit_id: int):
    return await service.toggle_archive(habit_id)
