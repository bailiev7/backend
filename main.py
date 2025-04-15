# main.py
from fastapi import FastAPI
import uvicorn
from router import router
from database import engine, Base

app = FastAPI()

# Создание таблиц при старте
Base.metadata.create_all(bind=engine)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
