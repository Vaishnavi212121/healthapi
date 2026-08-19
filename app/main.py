from fastapi import FastAPI
from app.routers.health_router import router
from app.middleware.logging_middleware import logging_middleware
from app.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)


app.middleware("http")(logging_middleware)

app.include_router(router)  #Connect the router to main.py

@app.get("/")
def root():
    return {
        "message": "System Health API is running"
    }