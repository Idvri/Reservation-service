import datetime

from pydantic import BaseModel


class CreateReservationSchema(BaseModel):
    """Модель брони для создания."""

    customer_name: str
    table_id: int
    duration_minutes: int


class ReservationSchema(CreateReservationSchema):
    """Модель брони для отображения."""

    id: int
    reservation_time: datetime.datetime
