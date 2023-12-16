from pydantic import BaseModel, Field
from uuid import uuid4

from sql_engine import SqlEngine

# Examples:
# 1)    name: month
#       description: Which month the media is in
#       input_source: RawImage
#       input_queue_name: InsightMonthJobs
#       output_queue_name: InsightMonthOutput - Consider to update the sql directly
# 2)    name: yolov7
#       description: Object in the image. Processed by yolov7 model, 79 available classes
#       input_source: RawImage
#       input_queue_name: InsightYolov7Jobs
#       output_queue_name: InsightYolov7Output
# 2)    name: face_recognition
#       description: A face in the media
#       input_source: InsightYolov7Output - Only class 0 (person)
#       queue_name: InsightFaceRJobs
class InsightEngine(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4())) #TODO: Consider regular integer
    name: str | None = None
    description: str | None = None
    input_source: str | None
    input_queue_name: str | None
    output_exchange_name: str | None
    
    @staticmethod
    def __sql_create_table__(environment: str):
        sql_template = """CREATE TABLE IF NOT EXISTS medias_"""+environment+""" (
            id VARCHAR ( 250 ) NOT NULL,
            name VARCHAR ( 250 ) NOT NULL,
            description TEXT,
            input_source ( 250 ) NOT NULL,
            input_queue_name ( 250 ) NOT NULL,
            output_queue_name ( 250 ) NOT NULL
        )"""
        return sql_template