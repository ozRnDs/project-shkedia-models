from insight_engine import InsightEngine

def test_insight_init_nominal():
    # SETUP
    engine_data = {
        "name": "test_engine",
        "input_source": "new_image.input",
        "input_queue_name": "TestInput",
        "output_exchange_name": "test.output"
    }

    # RUN
    new_insight_engine = InsightEngine(environment="dev", **engine_data)
    new_insight_engine2 = InsightEngine(environment="prd", **engine_data)
    # ASSERT
    assert new_insight_engine.table_name == "insightengines_dev"
    assert new_insight_engine2.table_name == "insightengines_prd"
    assert new_insight_engine2.id != new_insight_engine.id