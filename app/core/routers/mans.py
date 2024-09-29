from fastapi import APIRouter

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..models.db_helper import get_session
from ..models.mans import Man
from ..schemas.mans import ManSchema

router = APIRouter(
    prefix="/mans",
    tags=["Mans"]
    )

@router.get("/mans")
async def man_list(session: AsyncSession = Depends(get_session)):
    mans = await session.execute(select(Man))
    res = mans.scalars().all()
    return [ManSchema()]