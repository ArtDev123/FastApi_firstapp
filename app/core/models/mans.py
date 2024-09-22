from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import String, DateTime, ForeignKey, Table, Column, Text

from datetime import datetime
from typing import List

from .base import Base

category_man = Table(
    "category_man",
    Base.metadata,
    Column("cat_id", ForeignKey("categorys.id"), primary_key=True),
    Column("man_id", ForeignKey("mans.id"), primary_key=True)
)

class Category(Base):
    cat_name: Mapped[str] = mapped_column(String(20))
    mans: Mapped[List["Man"]] = relationship(
        secondary=category_man, back_populates="cats"
    )

class Man(Base):
    first_name: Mapped[str] = mapped_column(String(15))
    last_name: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(Text)
    categories: Mapped[List["Category"]] = relationship(
        secondary=category_man, back_populates = "mans"
    )
    created_on: Mapped[datetime] = mapped_column(DateTime, default = datetime.now)
    updated_on: Mapped[datetime] = mapped_column(DateTime, default = datetime.now, onupdate = datetime.now)