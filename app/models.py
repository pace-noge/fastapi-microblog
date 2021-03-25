from datetime import datetime
from sqlalchemy import (
    Column, Boolean, ForeignKey, Integer, String,
    DateTime
)
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(64), index=True, unique=True)
    password = Column(String(128))
    posts =  relationship('Post', backref='author', lazy='dynamic')


    def __repr__(self):
        return f"<User {self.username}"


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    body = Column(String(140))
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f"<Post {self.body}>"

