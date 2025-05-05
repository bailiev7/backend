from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from database import async_session_maker
from models.user import User as DBUser
from models.order import Order as DBOrder
from pydantic import BaseModel

user_router = APIRouter(prefix="/user")
order_router = APIRouter(prefix="/order")

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    age: int

class OrderCreate(BaseModel):
    user_id: int
    name: str
    sum: int

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
    
# ORDER ROUTES

@order_router.get("/all", response_model=list[OrderCreate])
async def get_all_orders():
    stmt = select(DBOrder)
    async with async_session_maker() as session:
        return (await session.scalars(stmt)).all()
    
@order_router.post("/create", response_model=OrderCreate)
async def create_order(order: OrderCreate):
    db_order = DBOrder(**order.dict())
    async with async_session_maker() as session:
        session.add(db_order)
        await session.commit()
    return db_order

@order_router.get("/get_by_name", response_model=list[OrderCreate])
async def get_order_by_name(name: str):
    stmt = select(DBOrder).where(DBOrder.name == name)
    async with async_session_maker() as session:
        users = (await session.scalars(stmt)).all()
    if not users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return users
    
@order_router.get("/by-user", response_model=list[OrderCreate])
async def get_orders_by_user(user_id: int):
    stmt = select(DBOrder).join(DBUser, DBOrder.user_id == DBUser.id).where(DBUser.id == user_id)
    async with async_session_maker() as session:
        return (await session.scalars(stmt)).all()