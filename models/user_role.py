from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base


class UserRole(Base):
    __tablename__ = "user_role"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_name = Column(String, nullable=False)
