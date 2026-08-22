from fastapi import FastAPI #imports the FastAPI class
from fastapi.middleware.cors import CORSMiddleware #Cross-Origin Resource Sharing-for allowing different origins.
from app.routers.health_router import router #mports the health router.
from app.middleware.logging_middleware import logging_middleware
#from app.settings import settings-imports your settings object.
from app.routers.auth_router import router as auth_router #imports the authentication router.


#Creates an instance/application object.
app = FastAPI( 
    title="System Health API", #sets the API title.
    version="1.0.0" #sets the API version.
)

app.add_middleware(  #Add this middleware to the FastAPI request/response pipeline.
    CORSMiddleware,   #for allowing different origins
    allow_origins=[
        "http://localhost:9000",
        "http://127.0.0.1:9000",
        "http://localhost:9003",
    ],
    allow_credentials=True, #allows credentials to be included in cross-origin requests.
    allow_methods=["*"], # * means all HTTP methods.
    allow_headers=["*"], #allows all request headers.
)

# Debug middleware
@app.middleware("http") #debugging middleware is used observe HTTP request and response while developing.
async def debug_middleware(request, call_next):

    print("========== REQUEST ==========")
    print("Method:", request.method)
    print("URL:", request.url)
    print("Origin:", request.headers.get("origin"))

    response = await call_next(request)

    print("========== RESPONSE ==========")
    print("Status:", response.status_code)

    return response


app.middleware("http")(logging_middleware)#Use this func as http middleware

app.include_router(router)  #Connect the router to main.py
app.include_router(auth_router)

@app.get("/") #decorator ,connects get / to root(), Whenever someone sends a GET request to /, execute root().
def root():
    return {
        "message": "System Health API is running"
    }