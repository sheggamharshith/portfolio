# fastapi
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# app core
from app.core import auth
from app.routes import views

# 3rd party imports 
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(views.router)


app.mount("/static", StaticFiles(directory="app/static"), name="static")

