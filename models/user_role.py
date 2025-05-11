from sqlalchemy import Column, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base
from models.role_enum import RoleEnum


class UserRole(Base):
    __tablename__ = "user_role"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_name = Column(Enum(RoleEnum, name="roleenum",
                       create_constraint=True), nullable=False, unique=True)
