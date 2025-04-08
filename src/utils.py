from typing import Any

from sqlalchemy import Sequence, select, Row, RowMapping
from sqlalchemy.orm import Session

from .config import db_session, Base


@db_session
def get_data(session: Session, table: Base) -> Sequence[Row[Any] | RowMapping | Any]:
    """Функция получения данных из БД."""

    query = select(table)
    data = session.execute(query)
    result = data.scalars().unique().all()

    return result


@db_session
def get_object(session: Session, table: Base, obj_id: int) -> Sequence | None:
    """Функция получения объекта из БД."""

    query = select(table).where(table.id == obj_id)
    data = session.execute(query)
    result = data.scalars().unique().one_or_none()

    return result


@db_session
def add_data(session: Session, table: Base, data: dict) -> Base:
    """Функция добавления данных в БД."""

    obj = table(**data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@db_session
def delete_data(session: Session, table: Base, main_id: int) -> None:
    """Функция удаления данных из БД."""

    data = session.query(table).filter_by(id=main_id).first()

    if data:
        session.delete(data)
        session.commit()
