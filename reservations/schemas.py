import datetime

from pydantic import BaseModel, Field, field_validator


class CreateReservationSchema(BaseModel):
    """Модель брони для создания."""

    customer_name: str
    table_id: int
    duration_minutes: int
    reservation_time: datetime.datetime = Field(example="2025-04-10 18:00:00")

    @field_validator('customer_name', mode="before")
    @classmethod
    def validate_customer_name(cls, value) -> str:
        """Валидация имени клиента."""

        if isinstance(value, str) is False:
            raise ValueError("Имя клиента должно быть строкой.")
        if not value:
            raise ValueError("Имя клиента не может быть пустым.")

        return value

    @field_validator('table_id', mode="before")
    @classmethod
    def validate_table_id(cls, value) -> int:
        """Валидация id столика."""

        if isinstance(value, int) is False:
            raise ValueError("Id столика должно быть числом.")
        if not value:
            raise ValueError("Id столика не может быть пустым.")

        return value

    @field_validator('reservation_time', mode="before")
    @classmethod
    def validate_reservation_time(cls, value) -> str:
        """Проверка даты и времени."""

        if isinstance(value, str) is False:
            raise ValueError('Дата и время должны быть указаны в формате строки. Пример: "2025-04-07 10:00:00".')

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

    @field_validator('duration_minutes', mode="before")
    @classmethod
    def validate_duration_minutes(cls, value) -> int:
        """Проверка длительности брони."""

        if not value:
            raise ValueError("Длительность брони не может быть пустой либо равной 0.")
        if value < 0:
            raise ValueError("Длительность брони не может быть отрицательной.")

        return value


class ReservationSchema(BaseModel):
    """Модель брони для отображения."""

    id: int
    customer_name: str
    table_id: int
    duration_minutes: int
    reservation_time: datetime.datetime
