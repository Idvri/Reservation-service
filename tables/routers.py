from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from src import get_data, add_data, delete_data
from .models import Table
from .schemas import CreateTableSchema, TableSchema

tables_router = APIRouter()


@tables_router.get("/tables/", response_model=List[TableSchema])
def get_tables():
    """Ручка для получения столиков из БД."""
    return get_data(Table)


@tables_router.post("/tables/", response_model=BaseModel)
def add_table(data: CreateTableSchema):
    """Ручка для добавления столика в БД."""
    add_data(Table, data.dict())
    return {"message": "Столик создан."}


@tables_router.delete("/tables/{table_id}", response_model=BaseModel)
def delete_table(table_id: int):
    """Ручка для удаления столика из БД."""
    delete_data(Table, table_id)
    return {"message": "Столик удален."}