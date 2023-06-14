
from fastapi import FastAPI
from routes.user_routes import user

app = FastAPI()
app.include_router(user)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
