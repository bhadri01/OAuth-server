from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserInDB(User):
    hashed_password: str


class UserLogin(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str
