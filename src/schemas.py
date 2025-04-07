from pydantic import BaseModel


class CreateTableSchema(BaseModel):
    """Модель столика для создания."""

    name: str
    seats: int
    location: str


class TableSchema(CreateTableSchema):
    """Модель столика для отображения."""

    id: int


class CreateReservationSchema(BaseModel):
    """Модель брони для создания."""

    customer_name: str
    table_id: int
    duration_minutes: int


class ReservationSchema(CreateReservationSchema):
    """Модель брони для отображения."""

    id: int
    reservation_time: str
    table: TableSchema
