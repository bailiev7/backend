from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from router import router
from typing import List


app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True) 
