from pydantic import BaseModel, Field, field_serializer
from uuid import uuid4
from datetime import datetime

class User(BaseModel):
    user_id: str = Field(default_factory=lambda: str(uuid4()))
    user_name: str
    created_on: str = Field(default_factory=lambda: datetime.now().isoformat())

    @field_serializer('created_on')
    def serialize_dates(self,field_value: datetime):
        if field_value:
            return field_value.isoformat()
        return None

class UserRequest(BaseModel):
    user_name: str
    password: str

class UserDB(User):
    password: str