from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Дочерний класс для создания пользователя
class User(BaseModel):
    first_name: str
    last_name: str
    age: int

# Имитация БД
user_table = [
    User(first_name="user1", last_name="last_name1", age=2135),
    User(first_name="user2", last_name="last_name1", age=55),
    User(first_name="user3", last_name="lastname_666", age=20),
]

# 1. Эндпоинт для вывода всех пользователей 
@router.get("/all", response_model=List[User])
async def get_all_users():
    return user_table

# 2. Эндпоинт для создания нового пользователя
@router.post("/create", response_model=User)
async def create_user(user: User):
    user_table.append(user)
    return user

# 3. Эндпоинт для поиска пользователя по имени
@router.get("/get_by_name", response_model=List[User])
async def get_user_by_name(first_name: str):
    found_users = [u for u in user_table if u.first_name == first_name]
    if not found_users:
        raise HTTPException(status_code=404, detail="User not found")
    return found_users