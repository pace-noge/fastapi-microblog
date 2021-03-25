import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or \
        "sqlite:///" + os.path.join(basedir, "microblog.db")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES") or 15
    ALGORITHM = os.environ.get("ALGORITHM") or "HS256"

