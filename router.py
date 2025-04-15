from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal
from models.user import User as DBUser

router = APIRouter()

# Pydantic модель для валидации данных
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    age: int

# Зависимость для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. Получить всех пользователей
@router.get("/all", response_model=list[UserCreate])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(DBUser).all()

# 2. Создать пользователя
@router.post("/create", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = DBUser(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 3. Найти по имени
@router.get("/get_by_name", response_model=list[UserCreate])
def get_user_by_name(first_name: str, db: Session = Depends(get_db)):
    users = db.query(DBUser).filter(DBUser.first_name == first_name).all()
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users
