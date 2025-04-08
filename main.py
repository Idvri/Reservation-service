from fastapi import FastAPI

from reservations import reservations_router
from tables import tables_router

app = FastAPI()
app.include_router(tables_router)
app.include_router(reservations_router)
