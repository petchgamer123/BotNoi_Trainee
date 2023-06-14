from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    user_id: str
    name: str
