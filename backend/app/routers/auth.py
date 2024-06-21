from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from app.database import users_collection
from app.models import User, UserInDB, Token,LoginRequest
from app.auth import verify_password, get_password_hash, create_access_token, decode_access_token
from pydantic import EmailStr

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/signup", response_model=Token)
async def signup(user: User):
    user_in_db = users_collection.find_one({"username": user.username})
    if user_in_db:
        raise HTTPException(
            status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(user.password)
    new_user = UserInDB(**user.dict(), hashed_password=hashed_password)
    users_collection.insert_one(new_user.dict())

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(login_request: LoginRequest):
    user = users_collection.find_one({"username": login_request.username})
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    user_in_db = UserInDB(**user)
    if not verify_password(login_request.password, user_in_db.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user_in_db.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/forgot-password")
async def forgot_password(email: EmailStr):
    user = users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=400, detail="Email not found")

    # Here you would send an email with a reset token
    reset_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=timedelta(minutes=10))
    # Send email logic goes here
    return {"msg": "Password reset token sent to email"}


@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    token_data = decode_access_token(token)
    if token_data is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = users_collection.find_one({"username": token_data.username})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user
