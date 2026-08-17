from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routers import items
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD APP")
app.include_router(items.router)
@app.get("/")
def root():
    return {"status": "running"}

