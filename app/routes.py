from app import app


@app.get("/")
@app.get("/index")
def index():
    return {"message": "Hello world"}

