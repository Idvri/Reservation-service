from sqlalchemy import Sequence, select
from sqlalchemy.orm import Session

from config import db_session, Base


@db_session
def get_data(session: Session, table: Base) -> Sequence:
    """Функция получения данных из БД."""

    query = select(table)
    data = session.execute(query)
    result = data.scalars().all()

    return result
