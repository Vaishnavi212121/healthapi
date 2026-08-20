from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.health_router import router
from app.middleware.logging_middleware import logging_middleware
from app.settings import settings
from app.routers.auth_router import router as auth_router

app = FastAPI(
    title="System Health API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:9000",
        "http://127.0.0.1:9000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.middleware("http")(logging_middleware)

app.include_router(router)  #Connect the router to main.py
app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "System Health API is running"
    }