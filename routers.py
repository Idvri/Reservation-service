from fastapi import APIRouter
from utils import get_data
from models import Table, Reservation

router = APIRouter()


@router.get("/tables/")
def get_tables():
    """Ручка для получения столиков из БД."""
    return get_data(Table)


@router.get("/reservations/")
def get_reservations():
    """Ручка для получения списка бронь из БД."""
    return get_data(Reservation)
