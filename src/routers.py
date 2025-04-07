from fastapi import APIRouter

from .utils import get_data, add_data
from .models import Table, Reservation
from .schemas import TableSchema, ReservationSchema

router = APIRouter()


@router.get("/tables/")
def get_tables():
    """Ручка для получения столиков из БД."""
    return get_data(Table)


@router.post("/tables/")
def add_table(data: TableSchema):
    """Ручка для добавления столика в БД."""
    add_data(Table, data.dict())
    return {"message": "Столик создан."}


@router.get("/reservations/")
def get_reservations():
    """Ручка для получения списка бронь из БД."""
    return get_data(Reservation)


@router.post("/reservations/")
def add_reservation(data: ReservationSchema):
    """Ручка для добавления брони в БД."""
    add_data(Reservation, data.dict())
    return {"message": "Столик забронирован."}
