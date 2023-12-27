from pydantic import BaseModel
from typing import List

from enum import Enum

class CollectionObjectEnum(str, Enum):
    CollectionBasic="CollectionBasic"
    CollectionPreview="CollectionPreview"


class CollectionBasic(BaseModel):
    name: str
    engine_name: str

class CollectionPreview(CollectionBasic):
    media_list: List[str] = []
    thumbnail: str | None = None