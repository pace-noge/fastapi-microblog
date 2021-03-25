from datetime import timedelta

from app.models import User
from app import schemas
from app import app
from core.utils import generate_access_token, oauth2_scheme
from fastapi import (
    Request, Depends, HTTPException, status
)
from fastapi.security import (
    OAuth2PasswordRequestForm
)
from sqlalchemy.orm import Session


from config import Config


def get_db(request: Request):
    return request.state.db


@app.get("/")
@app.get("/index")
def index():
    return {"message": "Hello world"}


@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if user is None or not user.verify_password(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Bearer"}
        )
    token_expires = timedelta(minutes=int(Config.ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = generate_access_token(
        data={"sub": user.username}, expires_delta=token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email Already registered"
        )
    new_user = User(username=user.username, email=user.email)
    new_user.set_password(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@app.get("/users/{id}", response_model=schemas.User)
async def read_user(id: int, db: Session = Depends(get_db), token: str =
               Depends(oauth2_scheme)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user.avatar = user.avatar()
    return user



@app.get("/items")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


