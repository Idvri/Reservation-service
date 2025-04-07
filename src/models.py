from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .config import Base


class Table(Base):
    """Стол в ресторане."""

    __tablename__ = 'table'

    id: Mapped[Integer] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[String] = mapped_column(String)
    seats: Mapped[Integer] = mapped_column(Integer)
    location: Mapped[String] = mapped_column(String)
    reservation: Mapped["Reservation"] = relationship(back_populates="table", uselist=False)


class Reservation(Base):
    """Бронь стола в ресторане."""

    __tablename__ = 'reservation'

    id: Mapped[Integer] = mapped_column(Integer, autoincrement=True, primary_key=True)
    customer_name: Mapped[String] = mapped_column(String)
    table_id: Mapped[Integer] = mapped_column(ForeignKey("table.id"), unique=True)
    table: Mapped["Table"] = relationship(back_populates="reservation")
    reservation_time: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    duration_minutes: Mapped[Integer] = mapped_column(Integer)
