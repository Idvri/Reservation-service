from pydantic import BaseModel, field_validator


class CreateTableSchema(BaseModel):
    """Модель столика для создания."""

    name: str
    seats: int
    location: str

    @field_validator('name', mode="before")
    @classmethod
    def validate_name(cls, value) -> str:
        """Валидация имени столика."""

        if isinstance(value, str) is False:
            raise ValueError("Имя столика должно быть строкой.")
        if not value:
            raise ValueError("Имя столика не может быть пустым.")

        return value

    @field_validator('seats', mode="before")
    @classmethod
    def validate_seats(cls, value) -> int:
        """Валидация количества мест."""

        if isinstance(value, int) is False:
            raise ValueError("Количество мест должно быть числом.")
        if value < 0:
            raise ValueError("Количество мест не может быть отрицательным.")
        if not value:
            raise ValueError("Количество мест не может быть пустым либо равно 0.")

        return value

    @field_validator('location', mode="before")
    @classmethod
    def validate_location(cls, value) -> str:
        """Валидация места расположения."""

        if isinstance(value, str) is False:
            raise ValueError("Место расположения должно быть строкой.")
        if not value:
            raise ValueError("Место расположения не может быть пустым.")

        return value


class TableSchema(BaseModel):
    """Модель столика для отображения."""

    id: int
    name: str
    seats: int
    location: str
