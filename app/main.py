from fastapi import FastAPI

from app.core.models.users import Man

app = FastAPI(
    title = "My first app"
)

@app.get('/hello')
async def hello():
    return {"message": "Hello Word"}

@app.get('/mans')
async def get_users(man_id: int | None = None):
    pass

# @app.post('/mans/{man_id}')
# async def create_man(man_id: int, name: str, role: str = "user"):
#     fake_users.append({
#         "id": man_id,
#         "role": role,
#         "name": name
#     })
#     return fake_users[man_id - 1]
