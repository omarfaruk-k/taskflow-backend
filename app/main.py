from fastapi import FastAPI
from app.api.routes import auth

app = FastAPI(title="TaskFlow API")

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "TaskFlow API is running"}