from fastapi import APIRouter

from .backend import fastapi_users, auth_backend
from .schemas import UserCreate, UserRead

router = APIRouter(
    prefix="/auth/jwt",
    tags=["Auth"]
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend)

)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate)
)