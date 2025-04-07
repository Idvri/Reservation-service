from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import Base


class Reservation(Base):
    """Бронь стола в ресторане."""

    __tablename__ = 'reservation'

    id: Mapped[Integer] = mapped_column(Integer, autoincrement=True, primary_key=True)
    customer_name: Mapped[String] = mapped_column(String)
    reservation_time: Mapped[DateTime] = mapped_column(DateTime)
    duration_minutes: Mapped[Integer] = mapped_column(Integer)
    table_id: Mapped[Integer] = mapped_column(ForeignKey("table.id"))
    table: Mapped["Table"] = relationship(back_populates="reservations")
