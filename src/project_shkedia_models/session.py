from pydantic import BaseModel, Field
from typing import Union
from uuid import uuid4
from datetime import datetime, timedelta

class Session(BaseModel):
    session_id: str = Field(default_factory=lambda:str(uuid4()))
    user_id: str
    device_id: str
    session_secret: str
    expiration_date: str = Field(default_factory=lambda:(datetime.now() + timedelta(days=7)).isoformat())
    last_activity: Union[str, None] = None

    
