from typing import List

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

from src import get_data, add_data, delete_data, get_object, DeleteSuccessResponse, ErrorResponse
from .models import Table
from .schemas import CreateTableSchema, TableSchema
from .utils import check_table_reservation

tables_router = APIRouter()


@tables_router.get(
    "/tables/", response_model=List[TableSchema]
)
def get_tables():
    """Ручка для получения столиков из БД."""
    return get_data(Table)


@tables_router.post("/tables/", response_model=TableSchema)
def add_table(data: CreateTableSchema):
    """Ручка для добавления столика в БД."""
    new_table = add_data(Table, data.dict())
    return TableSchema(**new_table.__dict__)


@tables_router.delete(
    "/tables/{table_id}",
    response_model=DeleteSuccessResponse,
    responses={HTTP_404_NOT_FOUND: {"model": ErrorResponse}, HTTP_409_CONFLICT: {"model": ErrorResponse}}
)
def delete_table(table_id: int):
    """Ручка для удаления столика из БД."""

    table = get_object(Table, table_id)
    if not table:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Столик не найден."
        )

    if not check_table_reservation(table_id):
        raise HTTPException(
            status_code=HTTP_409_CONFLICT,
            detail="На данный момент бронь по столику активна, "
                   "дождитесь окончания брони либо удалите её, перед удалением столика."
        )

    delete_data(Table, table_id)
    return {"message": "Столик удален."}
