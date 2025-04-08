from pydantic import BaseModel


class DeleteSuccessResponse(BaseModel):
    """Модель ответа успешного удаления."""

    message: str


class ErrorResponse(BaseModel):
    """Модель ответа ошибки."""

    status_code: int
    detail: str

