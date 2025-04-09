from fastapi import FastAPI

from reservations import reservations_router
from tables import tables_router

app = FastAPI(title="Сервис бронирования столов")
app.include_router(tables_router)
app.include_router(reservations_router)
