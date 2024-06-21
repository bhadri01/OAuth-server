from fastapi import FastAPI
from app.routers import auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])

# Add a root route


@app.get("/")
async def read_root():
    return {"message": "Welcome to the centralized authentication system"}
