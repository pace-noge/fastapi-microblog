from fastapi import FastAPI


app = FastAPI(title="Microblog")

from app import routes

