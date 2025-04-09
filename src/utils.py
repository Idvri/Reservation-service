from typing import Any

from sqlalchemy import Sequence, select, Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession

from .config import db_session, Base


@db_session
async def get_data(session: AsyncSession, table: Base) -> Sequence[Row[Any] | RowMapping | Any]:
    """Функция получения данных из БД."""

    query = select(table)
    data = await session.execute(query)
    result = data.scalars().unique().all()

    return result


@db_session
async def get_object(session: AsyncSession, table: Base, obj_id: int) -> Sequence | None:
    """Функция получения объекта из БД."""

    query = select(table).where(table.id == obj_id)
    data = await session.execute(query)
    result = data.scalars().unique().one_or_none()

    return result


@db_session
async def add_data(session: AsyncSession, table: Base, data: dict) -> Base:
    """Функция добавления данных в БД."""

    obj = table(**data)
    session.add(obj)
    await session.commit()
    await session.refresh(obj)
    return obj


@db_session
async def delete_data(session: AsyncSession, table: Base, main_id: int) -> None:
    """Функция удаления данных из БД."""

    stmt = select(table).filter_by(id=main_id)
    result = await session.execute(stmt)
    data = result.scalars().first()

    if data:
        await session.delete(data)
        await session.commit()
