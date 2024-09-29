from typing import Optional
from datetime import datetime

from fastapi_users import schemas

class UserRead(schemas.BaseUser[int]):
    username: str
    role_id: int
    registered_at: datetime

class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: int = 1

class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str] = None
    role_id: int
