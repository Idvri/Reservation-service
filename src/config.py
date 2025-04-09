from typing import Callable, Any

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeMeta, Session, declarative_base

Base: DeclarativeMeta = declarative_base()

DB_ENGINE = create_engine("postgresql+psycopg2://postgres:postgres@localhost/postgres")


def db_session(func: Callable) -> Callable:
    """Декоратор для работы с сессией БД."""

    def wrapper(*args, **kwargs) -> Any:
        with Session(DB_ENGINE) as session:
            res = func(session, *args, **kwargs)
            return res

    return wrapper
