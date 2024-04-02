from fastapi import FastAPI, HTTPException
from models import User, Gender, Roles
from uuid import UUID, uuid4

app = FastAPI()

db = [
    User(id=UUID("229f3e81-72b1-4c13-a15d-ded8f6a74966"), first_name="jamila", last_name="kane", middle_name="your_middle_name", gender=Gender.female, roles=[Roles.student]),
    User(id=UUID("a85b817e-4e66-4123-8da4-a6fae49589db"), first_name="james", last_name="arry", middle_name="demo", gender=Gender.female, roles=[Roles.admin, Roles.user])
]

@app.get("/")
async def root():
    return {"Hello": "junior"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id : {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, updated_user: User):
    for index, user in enumerate(db):
        if user.id == user_id:
            db[index] = updated_user
            return {"message": "User updated successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"user with id : {user_id} does not exist"
    )