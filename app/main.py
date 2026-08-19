from fastapi import FastAPI
from app.routers.health_router import router

app = FastAPI(
    title="System Health API",
    version="1.0.0"
)

app.include_router(router)  #Connect the router to main.py

@app.get("/")
def root():
    return {
        "message": "System Health API is running"
    }