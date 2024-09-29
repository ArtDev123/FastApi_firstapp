from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends, HTTPException, status

from core.models.db_helper import db_helper
from . import crud

async def get_product_by_id(
    product_id: int, 
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
    ):
    product = await crud.get_product(
        session=session, 
        product_id = product_id
    )

    if product is not None:
            return product
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found!"
    )