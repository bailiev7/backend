from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String)
    age = Column(Integer)
    role_id = Column(UUID(as_uuid=True), ForeignKey(
        "user_role.id"), nullable=True)
