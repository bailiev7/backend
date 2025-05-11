import uuid
from database import Base
from models.role_enum import RoleEnum
from sqlalchemy.orm import Mapped, mapped_column


class UserRole(Base):
    __tablename__ = "user_role"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    role_name: Mapped[RoleEnum] = mapped_column(unique=True)
