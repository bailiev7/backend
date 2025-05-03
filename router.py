from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_async_db
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
async def get_all_users(session: AsyncSession = Depends(get_async_db)):
    result = await session.execute(select(DBUser))
    return result.scalars().all()

@user_router.post("/create", response_model=UserCreate)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_async_db)):
    db_user = DBUser(**user.dict())
    session.add(db_user)
    await session.commit()
    return db_user

@user_router.get("/get_by_name", response_model=list[UserCreate])
async def get_user_by_name(first_name: str, session: AsyncSession = Depends(get_async_db)):
    result = await session.execute(select(DBUser).where(DBUser.first_name == first_name))
    users = result.scalars().all()
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users

# ORDER ROUTES

@order_router.get("/all", response_model=list[OrderCreate])
async def get_all_orders(session: AsyncSession = Depends(get_async_db)):
    result = await session.execute(select(DBOrder))
    return result.scalars().all()

@order_router.post("/create", response_model=OrderCreate)
async def create_order(order: OrderCreate, session: AsyncSession = Depends(get_async_db)):
    db_order = DBOrder(**order.dict())
    session.add(db_order)
    await session.commit()
    return db_order

@order_router.get("/get_by_name", response_model=list[OrderCreate])
async def get_order_by_name(name: str, session: AsyncSession = Depends(get_async_db)):
    result = await session.execute(select(DBOrder).where(DBOrder.name == name))
    orders = result.scalars().all()
    if not orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders

@order_router.get("/by-user", response_model=list[OrderCreate])
async def get_orders_by_user(user_id: int, session: AsyncSession = Depends(get_async_db)):
    orders = select(DBOrder).join(DBUser, DBOrder.user_id == DBUser.id).where(DBUser.id == user_id)
    return (await session.scalars(orders)).all()