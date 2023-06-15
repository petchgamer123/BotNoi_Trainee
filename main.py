
from fastapi import FastAPI
from routes.user_routes import user

from fastapi import FastAPI
from routes.user_routes import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user)

origins = [
    "https://b94f-180-183-117-81.ngrok-free.app",
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:4200/home",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
