from pydantic import BaseModel, EmailStr
from typing import Optional
from models.events import Event

class User(BaseModel):
  email: EmailStr
  password: str
  evnets: Optional[list[Event]]

  model_config = {
    "json_schema_extra": {
      "example": {
        "email": "fastAPI@gmail.com",
        "password": "f@st@PI1234",
        "evnets": []
      }
    }
  }

class UserSignIn(BaseModel):
  email: EmailStr
  password: str

  model_config = {
    "json_schema_extra": {
      "example": {
        "email": "fastAPI@gmail.com",
        "password": "f@st@PI1234"
      }
    }
  }