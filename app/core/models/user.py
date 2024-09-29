from datetime import datetime
from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from sqlalchemy import Integer, ForeignKey, DateTime, String, JSON

from core.config import DATABASE_URL
from core.models import Base

class Role(Base):
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    permissions: Mapped[dict] = mapped_column(JSON)

class User(SQLAlchemyBaseUserTable[int], Base):
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), default=1)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(cls, session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)