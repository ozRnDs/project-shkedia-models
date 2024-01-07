import os

from pydantic import BaseModel, Field
from typing import Any, Dict, List
from enum import Enum
class ActionsEnum(str, Enum):
    PUT="PUT"
    POST="POST"
    DEL="DEL"

class ProjectShkediaComponent(BaseModel):
    name: str
    id: str
    host_name: str = Field(default_factory=os.uname()[1])

class ProjectShkediaMsgMetadata(BaseModel):
    workers: List[ProjectShkediaComponent]
    timestamps: Dict[str,str] # Keys: process description, Value: ISO format datetime

class ProjectShkediaMessage(BaseModel):
    meta: ProjectShkediaMsgMetadata
    action: ActionsEnum
    body_type: str # The name of the class in the body as string (ex: project_shkedia_models.media.MediaIDs)
    body: List[Any] # List of objects of the body_type
