import pytest

from sqlalchemy_models import Media, User, Device, InsightEngine, Insight, InsightJob

@pytest.fixture(scope="module")
def user_fixture():
    new_user = User(user_name="TestUser", password="1234",
                    devices=[Device(device_name="android_device_1",
                                    device_status="ACTIVE"),
                            Device(device_name="Iphone 9", device_status="ACTIVE")])
    yield new_user

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

def test_add_media_to_user(user_fixture):
    new_media = Media(
        media_name="creative1",
        media_type="IMAGE",
        media_size_bytes="25004",
        media_width=1024,
        media_height=728,
        owner_id=user_fixture.user_id,
        device_id=user_fixture.devices[0].device_id,
        device_media_uri="url://test.com/creative1",
    )

    print(new_media)