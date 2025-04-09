from typing import List

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

from src import get_data, add_data, delete_data, get_object, DeleteSuccessResponse, ErrorResponse
from tables import Table
from .models import Reservation
from .schemas import CreateReservationSchema, ReservationSchema
from .utils import check_reservation_time

reservations_router = APIRouter()


@reservations_router.get("/reservations/", response_model=List[ReservationSchema], tags=["Бронирование"])
async def get_reservations():
    """Ручка для получения списка бронь из БД."""
    return await get_data(Reservation)


@reservations_router.post(
    "/reservations/",
    response_model=ReservationSchema,
    responses={HTTP_404_NOT_FOUND: {"model": ErrorResponse}, HTTP_409_CONFLICT: {"model": ErrorResponse}},
    tags=["Бронирование"]
)
async def add_reservation(data: CreateReservationSchema):
    """Ручка для добавления брони в БД."""

    if not await get_object(Table, data.table_id):
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Данный стол не существует."
        )

    if not await check_reservation_time(data.table_id, data.reservation_time):
        raise HTTPException(
            status_code=HTTP_409_CONFLICT,
            detail="На данное время стол занят."
        )

    new_reservation = await add_data(Reservation, data.dict())
    return ReservationSchema(**new_reservation.__dict__)


@reservations_router.delete(
    "/reservations/{reservation_id}",
    response_model=DeleteSuccessResponse,
    responses={HTTP_404_NOT_FOUND: {"model": ErrorResponse}},
    tags=["Бронирование"]
)
async def delete_reservation(reservation_id: int):
    """Ручка для удаления брони из БД."""

    reservation = await get_object(Reservation, reservation_id)
    if not reservation:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Бронь не найдена."
        )

    await delete_data(Reservation, reservation_id)
    return {"message": "Бронь удалена."}
