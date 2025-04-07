import datetime

from pydantic import BaseModel, field_validator


class CreateReservationSchema(BaseModel):
    """Модель брони для создания."""

    customer_name: str
    table_id: int
    duration_minutes: int
    reservation_time: datetime.datetime

    @field_validator('reservation_time', mode="before")
    @classmethod
    def validate_reservation_time(cls, value):
        """Проверка даты и времени."""

        if not value:
            raise ValueError("Дата и время не могут быть пустыми.")

        try:
            date = datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

        except ValueError:
            raise ValueError("Дата и время должны быть в формате YYYY-MM-DD HH:MM:SS, например: 2025-04-07 10:00:00")

        else:

            if date <= datetime.datetime.now():
                raise ValueError("Дата и время не могут быть меньше текущей.")

        return value


class ReservationSchema(BaseModel):
    """Модель брони для отображения."""

    id: int
    customer_name: str
    table_id: int
    duration_minutes: int
    reservation_time: datetime.datetime
