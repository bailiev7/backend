from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal
from models.user import User as DBUser
from models.order import Order as DBOrder


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#For User
user_router = APIRouter(prefix="/user")

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    age: int

@user_router.get("/all", response_model=list[UserCreate])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(DBUser).all()

@user_router.post("/create", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = DBUser(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user

@user_router.get("/get_by_name", response_model=list[UserCreate])
def get_user_by_name(first_name: str, db: Session = Depends(get_db)):
    users = db.query(DBUser).filter(DBUser.first_name == first_name).all()
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users


#For Order
order_router = APIRouter(prefix="/order")

class OrderCreate(BaseModel):
    user_id: int
    name: str
    sum: int

@order_router.get("/all", response_model=list[OrderCreate])
def get_all_orders(db: Session = Depends(get_db)):
    return db.query(DBOrder).all()

@order_router.post("/create", response_model=OrderCreate)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = DBOrder(**order.dict())
    db.add(db_order)
    db.commit()
    return db_order

@order_router.get("/get_by_name", response_model=list[OrderCreate])
def get_order_by_name(name: str, db: Session = Depends(get_db)):
    orders = db.query(DBOrder).filter(DBOrder.name == name).all()
    if not orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders
