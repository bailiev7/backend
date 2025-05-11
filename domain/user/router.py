from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from database import async_session_maker
from models.user import User as DBUser
from pydantic import BaseModel

user_router = APIRouter(prefix="/user")


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    age: int

# USER ROUTES


@user_router.get("/all", response_model=list[UserCreate])
async def get_all_users():
    stmt = select(DBUser)
    async with async_session_maker() as session:
        return (await session.scalars(stmt)).all()


@user_router.post("/create", response_model=UserCreate)
async def create_user(user: UserCreate):
    db_user = DBUser(**user.dict())
    async with async_session_maker() as session:
        session.add(db_user)
        await session.commit()
    return db_user


@user_router.get("/get_by_name", response_model=list[UserCreate])
async def get_user_by_name(last_name: str):
    stmt = select(DBUser).where(DBUser.last_name == last_name)
    async with async_session_maker() as session:
        users = (await session.scalars(stmt)).all()
    if not users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return users
