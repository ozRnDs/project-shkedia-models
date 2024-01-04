from pydantic import BaseModel, Field, field_serializer
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

    @field_serializer('create_on')
    def serialize_dates(self,field_value: datetime):
        if field_value:
            return field_value.isoformat()
        return None