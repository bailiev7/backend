from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from database import async_session_maker
from models.user import User as DBUser
from pydantic import BaseModel, field_validator
from models.role_enum import RoleEnum
from models.user_role import UserRole

user_router = APIRouter(prefix="/user")


class SetUserRoleRequest(BaseModel):
    user_id: int
    role: str

    @field_validator("role")
    def normalize_role(cls, value: str) -> str:
        value = value.lower()
        if value not in ("admin", "default_user"):
            raise ValueError("role must be 'admin' or 'default_user'")
        return value


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
async def get_user_by_name(first_name: str):
    stmt = select(DBUser).where(DBUser.first_name == first_name)
    async with async_session_maker() as session:
        users = (await session.scalars(stmt)).all()
    if not users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return users


@user_router.post("/set/role")
async def set_role(data: SetUserRoleRequest):
    stmt_user = select(DBUser).where(DBUser.id == data.user_id)
    stmt_role = select(UserRole).where(
        UserRole.role_name == data.role)
    async with async_session_maker() as session:
        user = (await session.scalars(stmt_user)).first()
        if user is None:
            raise HTTPException(
                status_code=404, detail="Пользователь не найден")
        role = (await session.scalars(stmt_role)).first()
        if role is None:
            raise HTTPException(status_code=404, detail="Роль не найдена")
        user.role_id = role.id
        await session.commit()
        await session.refresh(user)

    return {"message": f"Пользователю {user.first_name} назначена роль {data.role.value}"}
