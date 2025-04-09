import datetime

from src import get_object

from .models import Table


async def check_table_reservation(table_id) -> bool:
    """Проверка наличия брони по столику, в данный момент времени."""

    table = await get_object(Table, table_id)

    for reservation in table.reservations:
        current_time = datetime.datetime.now()
        start_time = reservation.reservation_time
        end_time = reservation.reservation_time + datetime.timedelta(reservation.duration_minutes)
        if start_time <= current_time <= end_time:
            return False

    return True
