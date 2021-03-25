**Install requirements**
------------------------
```bash
poetry install
```


**Run Server**
--------------

```
uvicorn main:app
```

**Special Note for Alembic**
----------------------------

```bash
# make migrations
alembic revision --atuogenerate -m "message her"

# apply migration
alembic upgrade head

```


