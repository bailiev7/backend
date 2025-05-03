from fastapi import FastAPI
import uvicorn
from database import engine, Base
from router import user_router, order_router


app = FastAPI()

app.include_router(user_router)
app.include_router(order_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)