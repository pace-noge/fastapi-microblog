from fastapi import FastAPI, Depends, HTTPException
from app.db import SessionLocal, engine
from . import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Microblog")

from app import middlewares, routes

