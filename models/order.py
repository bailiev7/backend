from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    sum = Column(Integer)
