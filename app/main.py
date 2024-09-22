from fastapi import FastAPI

from core.models.mans import Man

from core.auth.routers import router
from core.auth.manager import get_user_manager
from core.auth.backend import auth_backend

from fastapi_users import FastAPIUsers
from core.models.users import User


app = FastAPI()

@app.get('/hello')
async def hello():
    return {"message": "Hello Word"}

@app.get('/mans')
async def get_users(man_id: int | None = None):
    pass

app.include_router(router)
# @app.post('/mans/{man_id}')
# async def create_man(man_id: int, name: str, role: str = "user"):
#     fake_users.append({
#         "id": man_id,
#         "role": role,
#         "name": name
#     })
#     return fake_users[man_id - 1]
