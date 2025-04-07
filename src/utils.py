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


@db_session
def delete_data(session: Session, table: Base, main_id: int) -> None:
    """Функция удаления данных из БД."""

    data = session.query(table).filter_by(id=main_id).first()

    if data:
        session.delete(data)
        session.commit()
