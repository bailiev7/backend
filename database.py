from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение к PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgresql:bailiev@localhost/bailiev"

# Создание движка
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс
Base = declarative_base()
