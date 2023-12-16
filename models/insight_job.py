from pydantic import BaseModel, Field
from uuid import uuid4
from enum import Enum
from datetime import datetime

class JobStatus(Enum, str):
    PENDING="PENDING"
    DONE="DONE"
    FAILED="FAILED"

# Process Requirements:
# The job should be started by the insights-schedular.
# There are two types of jobs:
# 1) Job on an image
# 2) Job on a parent insight (for example, face detection should be done on persons)
# There are two ways to start a job:
# 1) Batch Start - Every 2-3 hours the scheduler searches for insights that need to be processes, and send a mission to the queue
# 2) On Demand Start - New image/Parent insight was registered and should be processed. Dedicated queue should be ready for those cases

# Examples:
# 1)    id: int = 1
#       media_id: str
#       insight_engine_id: str
#       status: Enum (str) | None = NONE, PENDING, DONE
# 1)    id: int = 2
#       media_id: str
class InsightJob(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4())) #TODO: Consider regular integer
    media_id: str
    insight_engine_id: str
    status: JobStatus | None = JobStatus.PENDING
    start_time: datetime = Field(default_factory=lambda: datetime.now())
    end_time: datetime | None = None
    net_time_seconds: int | None = None