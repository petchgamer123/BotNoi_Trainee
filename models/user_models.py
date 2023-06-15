from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    name: str
    age: str
    gender: str

class data(BaseModel):
    age: str
    gender: str

