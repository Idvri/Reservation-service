from pydantic import BaseModel


class TableSchema(BaseModel):
    """Модель столика."""

    name: str
    seats: int
    location: str


class ReservationSchema(BaseModel):
    """Модель брони."""

    customer_name: str
    table_id: int
    duration_minutes: int
