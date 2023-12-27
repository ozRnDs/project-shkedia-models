from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime

class User(BaseModel):
    user_id: str = Field(default_factory=lambda: str(uuid4()))
    user_name: str
    created_on: str = Field(default_factory=lambda: datetime.now().isoformat())

class UserRequest(BaseModel):
    user_name: str
    password: str

class UserDB(User):
    password: str