from fastapi import FastAPI, HTTPException
import uvicorn
<<<<<<< HEAD
=======
from pydantic import BaseModel
>>>>>>> 4c7437c152d32eac1816cc8149624a99cc61c084
from router import router
from typing import List


app = FastAPI()

app.include_router(router)

<<<<<<< HEAD
=======

class User(BaseModel):
    first_name: str
    last_name: str
    age: int


user_table = [
    User(first_name="user1", last_name="last_name1", age=2135),
    User(first_name="user2", last_name="last_name1", age=55),
    User(first_name="user3", last_name="lastname_666", age=20),
]


@app.get("/all", response_model=List[User])
async def get_all_users():
    return user_table

# 2. Эндпоинт для создания нового пользователя
@app.post("/create", response_model=User)
async def create_user(user: User):
    user_table.append(user)
    return user

# 3. Эндпоинт для поиска пользователя по имени
@app.get("/get_by_name", response_model=List[User])
async def get_user_by_name(first_name: str):
    found_users = [u for u in user_table if u.first_name == first_name]
    if not found_users:
        raise HTTPException(status_code=404, detail="User not found")
    return found_users

>>>>>>> 4c7437c152d32eac1816cc8149624a99cc61c084
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) 
