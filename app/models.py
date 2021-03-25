from datetime import datetime
from sqlalchemy import (
    Column, Boolean, ForeignKey, Integer, String,
    DateTime
)
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from hashlib import md5

from core.db import Base


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(64), index=True, unique=True)
    password = Column(String(128))
    posts =  relationship('Post', back_populates='user')
    about_me = Column(String(140))
    last_seen = Column(DateTime, default=datetime.utcnow)


    def set_password(self, password):
        self.password = pwd_context.hash(password)


    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def avatar(self, size=128):
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"


    def __repr__(self):
        return f"<User {self.username}>"


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    body = Column(String(140))
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post {self.body}>"

