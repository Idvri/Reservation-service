from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from .utils import get_data, add_data, delete_data
from .models import Table, Reservation
from .schemas import CreateTableSchema, TableSchema, CreateReservationSchema, ReservationSchema

router = APIRouter()


@router.get("/tables/", response_model=List[TableSchema])
def get_tables():
    """Ручка для получения столиков из БД."""
    return get_data(Table)


@router.post("/tables/", response_model=BaseModel)
def add_table(data: CreateTableSchema):
    """Ручка для добавления столика в БД."""
    add_data(Table, data.dict())
    return {"message": "Столик создан."}


@router.delete("/tables/{table_id}", response_model=BaseModel)
def delete_table(table_id: int):
    """Ручка для удаления столика из БД."""
    delete_data(Table, table_id)
    return {"message": "Столик удален."}


@router.get("/reservations/", response_model=List[ReservationSchema])
def get_reservations():
    """Ручка для получения списка бронь из БД."""
    return get_data(Reservation)


@router.post("/reservations/", response_model=BaseModel)
def add_reservation(data: CreateReservationSchema):
    """Ручка для добавления брони в БД."""
    add_data(Reservation, data.dict())
    return {"message": "Столик забронирован."}


@router.delete("/reservations/{reservation_id}", response_model=BaseModel)
def delete_reservation(reservation_id: int):
    """Ручка для удаления брони из БД."""
    delete_data(Reservation, reservation_id)
    return {"message": "Бронь удалена."}
