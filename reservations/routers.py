from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from src import get_data, add_data, delete_data
from .models import Reservation
from .schemas import CreateReservationSchema, ReservationSchema

reservations_router = APIRouter()


@reservations_router.get("/reservations/", response_model=List[ReservationSchema])
def get_reservations():
    """Ручка для получения списка бронь из БД."""
    return get_data(Reservation)


@reservations_router.post("/reservations/", response_model=BaseModel)
def add_reservation(data: CreateReservationSchema):
    """Ручка для добавления брони в БД."""
    add_data(Reservation, data.dict())
    return {"message": "Столик забронирован."}


@reservations_router.delete("/reservations/{reservation_id}", response_model=BaseModel)
def delete_reservation(reservation_id: int):
    """Ручка для удаления брони из БД."""
    delete_data(Reservation, reservation_id)
    return {"message": "Бронь удалена."}
