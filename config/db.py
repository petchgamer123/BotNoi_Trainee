from pymongo import MongoClient
from decouple import config

Client = MongoClient("mongodb+srv://petchgamer2544:ITHZVfbukRUxAoKh@cluster0.vypdt9h.mongodb.net/?retryWrites=true&w=majority")

db = Client.dataBase_user

collection_name = db["user"]

