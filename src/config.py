from typing import Callable, Any
from functools import wraps

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()

DB_ENGINE = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@localhost/postgres",
    echo=False,
)

AsyncSessionLocal = async_sessionmaker(
    bind=DB_ENGINE,
    class_=AsyncSession,
    expire_on_commit=False,
)


def db_session(func: Callable) -> Callable:
    """Асинхронный декоратор для работы с сессией БД."""

    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        async with AsyncSessionLocal() as session:
            return await func(session, *args, **kwargs)

    return wrapper
