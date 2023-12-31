from pydantic import BaseModel, Field, field_serializer
from typing import Union, TypeVar, Type, List
from uuid import uuid4
from datetime import datetime, timedelta

from enum import Enum

class InsightJobStatus(str, Enum):
    PENDING="PENDING"
    DONE="DONE"
    CANCELED="CANCELED"
    FAILED="FAILED"

class InsightJob(BaseModel):
    id: str = Field(default_factory=lambda:str(uuid4()))
    insight_engine_id: str
    media_id: str
    status: InsightJobStatus = InsightJobStatus.PENDING
    start_time: datetime = Field(default_factory=lambda:datetime.now())
    end_time: datetime | None = None
    net_time_seconds: datetime | None = None

    @field_serializer('start_time',"end_time", "net_time_seconds")
    def serialize_dates(self,field_value: datetime):
        if field_value:
            return field_value.isoformat()
        return None