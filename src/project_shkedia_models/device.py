from pydantic import BaseModel, Field
from typing import Union
from uuid import uuid4
from datetime import datetime

class DeviceRequest(BaseModel):
    device_name: str
    owner_name: str

class Device(BaseModel):
    device_id: str = Field(default_factory=lambda:str(uuid4()))
    device_name: str
    owner_id: str
    created_on: datetime = Field(default_factory=lambda:datetime.now().isoformat())
    status: str = "ACTIVE"