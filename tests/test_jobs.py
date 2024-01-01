from datetime import datetime

from jobs import InsightJob


def test_job_serial_end_none():
    # SETUP
    new_job = InsightJob(insight_engine_id="testing",
                              media_id="tesing_media")
    
    # Run
    new_dump = new_job.model_dump()

    assert type(new_dump) == dict
    assert new_dump["insight_engine_id"]==new_job.insight_engine_id
    assert type(new_dump["start_time"]) == str
    assert type(new_dump["end_time"]) == type(None)

def test_job_serial():
    # SETUP
    new_job = InsightJob(insight_engine_id="testing",
                              media_id="tesing_media",
                              end_time=datetime(year=2023,month=10,day=5))
    
    # Run
    new_dump = new_job.model_dump()

    assert type(new_dump) == dict
    assert new_dump["insight_engine_id"]==new_job.insight_engine_id
    assert type(new_dump["start_time"]) == str
    assert type(new_dump["end_time"]) == str