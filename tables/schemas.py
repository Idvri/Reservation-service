from pydantic import BaseModel


class CreateTableSchema(BaseModel):
    """Модель столика для создания."""

    name: str
    seats: int
    location: str


class TableSchema(CreateTableSchema):
    """Модель столика для отображения."""

    id: int
