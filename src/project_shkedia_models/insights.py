from pydantic import BaseModel, Field
from typing import List
from uuid import uuid4

from enum import Enum

class InsightEngineStatus(str, Enum):
    ACTIVE="ACTIVE"
    INACTIVE="INACTIVE"

class InsightEngineObjectEnum(str, Enum):
    InsightEngineBasic="InsightEngineBasic"
    InsightEngine="InsightEngine"
    InsightEngineValues="InsightEngineValues"

class InsightObjectEnum(str, Enum):
    InsightBasic="InsightBasic"
    Insight="Insight"

class InsightStatusEnum(str, Enum):
    PREDICTED="PREDICTED"
    APPROVED="APPROVED"
    REJECTED="REJECTED"

class InsightEngineBasic(BaseModel):
    id: str = Field(default_factory=lambda:str(uuid4()))
    name: str
    status: InsightEngineStatus = InsightEngineStatus.ACTIVE

    class Config:
        use_enum_values = True
        validate_assignment = True

class InsightEngineValues(InsightEngineBasic):
    insights_names: List[str] = []

class InsightEngine(InsightEngineBasic):
    description: str
    input_source: str
    input_queue_name: str
    output_exchange_name: str

class InsightBasic(BaseModel):
    id: str = Field(default_factory=lambda:str(uuid4()))
    insight_engine_id: str
    job_id: str
    media_id: str
    name: str
    prob: float | None = None
    status: InsightStatusEnum = InsightStatusEnum.PREDICTED

    class Config:
        use_enum_values = True
        validate_assignment = True

class Insight(InsightBasic):
    bounding_box: str | None = None
    description: str | None = None
