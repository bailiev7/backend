from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

# Подключение к PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:bailiev@localhost:5432/bailiev"

# Базовый класс
Base = declarative_base()

engine = create_async_engine(SQLALCHEMY_DATABASE_URL,
                             echo=True,
                             pool_size=10,
                             pool_pre_ping=True,
                             max_overflow=0, future=True
)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
