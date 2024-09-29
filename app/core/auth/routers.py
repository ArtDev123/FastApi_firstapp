from fastapi import APIRouter

from .backend import auth_backend
from .schemas import UserCreate, UserRead, UserUpdate
from .utils import get_user_manager
from ..models.user import User

from fastapi_users import FastAPIUsers

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=False)
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate)
)

router.include_router(
    fastapi_users.get_verify_router(UserRead)
)

router.include_router(
    fastapi_users.get_reset_password_router()
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate)
)

current_user = fastapi_users.current_user()