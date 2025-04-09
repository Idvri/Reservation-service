from datetime import timedelta

from src import get_object
from tables import Table


async def check_reservation_time(table_id, reservation_time):
    """Проверка конфликтов во времени брони."""

    table = await get_object(Table, table_id)

    for reservation in table.reservations:

        due_time = reservation.reservation_time + timedelta(minutes=reservation.duration_minutes)
        if reservation.reservation_time <= reservation_time <= due_time:
            return False

    return True
