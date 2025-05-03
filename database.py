from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Подключение к PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgresql:bailiev@localhost/bailiev"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# Базовый класс
Base = declarative_base()

async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session
