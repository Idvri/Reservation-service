from typing import List

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src import Base


class Table(Base):
    """Стол в ресторане."""

    __tablename__ = 'table'

    id: Mapped[Integer] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[String] = mapped_column(String)
    seats: Mapped[Integer] = mapped_column(Integer)
    location: Mapped[String] = mapped_column(String)
    reservations: Mapped[List["Reservation"]] = relationship(
        back_populates="table",
        lazy="joined",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
