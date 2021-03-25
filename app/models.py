from sqlalchemy import (
    Column, Boolean, ForeignKey, Integer, String
)
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(64), index=True, unique=True)
    password = Column(String(128))


    def __repr__(self):
        return f"<User {self.username}"

