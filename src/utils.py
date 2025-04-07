from sqlalchemy import Sequence, select
from sqlalchemy.orm import Session

from .config import db_session, Base


@db_session
def get_data(session: Session, table: Base) -> Sequence:
    """Функция получения данных из БД."""

    query = select(table)
    data = session.execute(query)
    result = data.scalars().all()

    return result


@db_session
def add_data(session: Session, table: Base, data: dict) -> None:
    """Функция добавления данных в БД."""

    session.add(table(**data))
    session.commit()
