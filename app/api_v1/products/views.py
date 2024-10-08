from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial
from core.models.db_helper import db_helper
from .dependencies import get_product_by_id

router = APIRouter(tags=["Products"])

@router.get(
    "/",
    response_model=list[Product]
)
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_products(session=session)

@router.get(
    "/{product_id}", 
    response_model=Product
)
async def get_product(
    product: Product = Depends(get_product_by_id)
):
    return product

@router.post(
    "/", 
    response_model=Product
)
async def create_product(
     product_in: ProductCreate, 
     session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_product(session=session, product_in=product_in)

@router.put("/{product_id}")
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(get_product_by_id),
    session: AsyncSession = Depends(db_helper.get_scoped_session)
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update
    )

@router.patch("/{product_id}")
async def update_product_partial(
    product_update: ProductUpdatePartial,
    product: Product = Depends(get_product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True
    )

@router.delete("/{product_id}")
async def delete_product(
    product: Product = Depends(get_product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.delete_product(
        session=session,
        product=product
    )