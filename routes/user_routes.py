from fastapi import APIRouter
from api.api import response_7Days, resultToDay, responseTest
from models.user_models import User, data
from config.db import collection_name
from schemas.user_schemas import user_serializer, users_serializer

# from auth.jwt_handler import signJWT
# from auth.jwt_bearer import JWTBearer  ยังไม่ใช้


from decouple import config
from bson import ObjectId

user = APIRouter()
API_KEY2 = config("API_KEY_WEATHER")



# ********************** แก้ **********************
# @user.get("/weather")
# def get_weather():
#     weather_data = result(response)
#     return response
# ********************** แก้ **********************
# ************************************************
@user.get("/weather/Days", tags=["weather"])
def get_weather():
    return response_7Days
# ************************************************
@user.get("/{country}", tags=["weather"])
def country(country: str):
    url = responseTest(country)
    return resultToDay(url)
# ************************************************

@user.get("/get/", tags=["user"])
async def get_users():
    users = users_serializer(collection_name.find())
    return {"status": "OK", "data":users}

@user.post("/post/", tags=["user"])
async def post_users(user: User):
    _id = collection_name.insert_one(dict(user))
    users = users_serializer(collection_name.find({"_id": _id.inserted_id}))
    return {"status": "OK", "data":users}

@user.get("/findname/{id}", tags=["user"])
async def get_one_user(id: str):
    user = collection_name.find_one({"user_id": id}, {'_id': False})
    return {"status": "OK", "data":user}

@user.put("/updateUser/{id}", tags=["user"])
async def update_user(id: str, user:data):
    collection_name.find_one_and_update({"user_id": id}, {
        "$set": dict(user)
    })
    user = users_serializer(collection_name.find({"user_id": id}))
    return {"status": "OK", "data": user}

@user.delete("/deleteUser/{id}", tags=["user"])
async def delete_user(id: str):
    collection_name.find_one_and_delete({"user_id": id})
    return {"status": "ok"}

