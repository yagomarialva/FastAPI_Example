from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Roles, User

app = FastAPI()

db: List[User] = [
    User(id="8bcdfcd4-036c-4f80-ae4c-81d47a445c4b",
         first_name="Jamila",
         last_name="Armed",
         gender=Gender.female,
         roles=[Roles.student]),

    User(id=uuid4(),
         first_name="cf39b6e5-ec3e-4907-9127-f4b370a3872b",
         last_name="FON",
         gender=Gender.male,
         roles=[Roles.user.admin]),
]


@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;