from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from src import get_data, add_data, delete_data, get_object
from tables import Table
from .models import Reservation
from .schemas import CreateReservationSchema, ReservationSchema
from .utils import check_reservation_time

reservations_router = APIRouter()


@reservations_router.get("/reservations/", response_model=List[ReservationSchema])
def get_reservations():
    """Ручка для получения списка бронь из БД."""
    return get_data(Reservation)


@reservations_router.post("/reservations/", response_model=BaseModel)
def add_reservation(data: CreateReservationSchema):
    """Ручка для добавления брони в БД."""

    if not get_object(Table, data.table_id):
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Данный стол не существует."
        )

    if not check_reservation_time(data.table_id, data.reservation_time):
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail="На данное время стол занят."
        )

    add_data(Reservation, data.dict())
    return {"message": "Столик забронирован."}


@reservations_router.delete("/reservations/{reservation_id}", response_model=BaseModel)
def delete_reservation(reservation_id: int):
    """Ручка для удаления брони из БД."""

    reservation = get_object(Reservation, reservation_id)
    if not reservation:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Бронь не найдена."
        )

    delete_data(Reservation, reservation_id)
    return {"message": "Бронь удалена."}
