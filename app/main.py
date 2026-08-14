from fastapi import FastAPI

app = FastAPI(title="CRUD APP")

@app.get("/")
def root():
    return {"status": "running"}