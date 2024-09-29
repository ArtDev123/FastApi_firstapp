from fastapi import FastAPI

from core.auth import router as auth_router
from api_v1 import router as product_router
from core.config import settings

app = FastAPI()

@app.get('/hello')
async def hello():
    return {"message": "Hello Word"}

@app.get('/mans')
async def get_users(man_id: int | None = None):
    pass

app.include_router(auth_router)
app.include_router(product_router, prefix=settings.api_v1_prefix)
# @app.post('/mans/{man_id}')
# async def create_man(man_id: int, name: str, role: str = "user"):
#     fake_users.append({
#         "id": man_id,
#         "role": role,
#         "name": name
#     })
#     return fake_users[man_id - 1]
