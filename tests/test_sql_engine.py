import pytest

from sql_engine import SqlEngine
from insight_engine import InsightEngine

@pytest.fixture(scope="module")
def insight_engine_fixture():
    engine_data = {
        "name": "test_engine",
        "input_source": "new_image.input",
        "input_queue_name": "TestInput",
        "output_exchange_name": "test.output"
    }
    insight_engine_object = InsightEngine(**engine_data)
    yield insight_engine_object

def test_sql_engine_insert_nominal(insight_engine_fixture):
    # SETUP

    test_sql_engine = SqlEngine()

    # RUN
    sql_template, values = test_sql_engine.__sql_insert__(insight_engine_fixture)

    # ASSERT
    assert sql_template == "INSERT INTO insightengines_dev (id,name,input_source,input_queue_name,output_exchange_name) VALUES (%s,%s,%s,%s,%s)"
    assert values[1:] == ('test_engine', 'new_image.input', 'TestInput', 'test.output')

def test_sql_engine_update_nominal(insight_engine_fixture):
    # SETUP
    test_sql_engine = SqlEngine()
    update_dictionary = {
        "name": "updated_name"
    }
    # RUN
    sql_template, values = test_sql_engine.__sql_update_item__(object=insight_engine_fixture, update_dictionary=update_dictionary)
    # ASSERT
    assert sql_template == "UPDATE insightengines_dev SET name=%s WHERE id=%s"
    assert values[:-1] == ('updated_name',)
    assert len(values) == 2