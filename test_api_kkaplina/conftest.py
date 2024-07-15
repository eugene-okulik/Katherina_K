import pytest
from test_api_kkaplina.endpoints.create_object import CreateObject
from test_api_kkaplina.endpoints.update_object import UpdateObject
from test_api_kkaplina.endpoints.partial_update_object import PartialUpdateObject
from test_api_kkaplina.endpoints.delete_object import DeleteObject
from test_api_kkaplina.endpoints.get_object import GetRequestObject

url = 'https://api.restful-api.dev/objects'


@pytest.fixture()
def post_create_object():
    return CreateObject()


@pytest.fixture()
def put_update_object():
    return UpdateObject()


@pytest.fixture()
def patch_update_object():
    return PartialUpdateObject()

@pytest.fixture()
def get_request_object():
    return GetRequestObject()

@pytest.fixture()
def delete_object():
    return DeleteObject()


@pytest.fixture()
def new_object_id(post_create_object, delete_object):
    payload = {
        "name": "NEW - Apple MacBook Pro 2024 Kate",
        "data": {
            "year": 2024,
            "price": 200,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = post_create_object.new_object(payload)
    object_id = response.json()['id']
    yield object_id
    delete_object.delete_object_by_id(f'{object_id}')