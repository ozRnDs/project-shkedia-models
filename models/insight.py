from pydantic import BaseModel, Field
from typing import List
from uuid import uuid4


# Examples:
# 1)    insight_engine_id: 1 (month engine for example)
#       media_id: jg545gkj-gkjglkjdgqwe-rtwret (The media the insight is related to).
#       insight_name: 08-2023 (The name of the object or property for the image)
#       boundingbox: None (The bounding box in the original image, not relevant for month-engine)
# 2)    insight_engine_id: 1 (yolov7 for example)
#       media_id: jg545gkj-gkjglkjdgqwe-rtwret (The media the insight is related to).
#       insight_name: horse (The name of the object or property for the image)
#       boundingbox: [25,40,250,180]
# 2b)   insight_engine_id: 1 (yolov7 for example)
#       media_id: jg545gkj-gkjglkjdgqwe-rtwret (The media the insight is related to).
#       insight_name: horse (The name of the object or property for the image)
#       boundingbox: [500,340,800,1000] (The bounding box proportional to the original image)
# 3)    insight_engine_id: 3 (face_recognition)
#       media_id: jg545gkj-gkjglkjdgqwe-rtwret (The media the insight is related to).
#       insight_name: person_name? key? need a discussion. 
#       boundingbox: [245,430,450,700] (The bounding box of the original image)
class Insight(BaseModel):
    insight_engine_id: str
    media_id: str
    name: str | None = None
    description: str | None = None
    queue_name: str | None = None
    bounding_box: List[int] = None
    