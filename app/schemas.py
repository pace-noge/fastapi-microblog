from pydantic import BaseModel
from typing import Optional, List, Callable


class PostBase(BaseModel):
    body: str
    timestamp: str


class Post(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    posts: List[Post] = []
    avatar: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

