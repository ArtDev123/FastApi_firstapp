from datetime import datetime
from typing import AsyncGenerator, TYPE_CHECKING
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import Integer, ForeignKey, DateTime, String, JSON

from core.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from .base import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class Role(Base):
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    permissions: Mapped[dict] = mapped_column(JSON)

class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    @classmethod
    async def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)






