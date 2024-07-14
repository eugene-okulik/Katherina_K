import pytest
import requests
from project.Katherina_K.test_api_kkaplina.endpoints.create_object import CreateObject
from project.Katherina_K.test_api_kkaplina.endpoints.update_object import UpdateObject
from project.Katherina_K.test_api_kkaplina.endpoints.partial_update_object import PartialUpdateObject
from project.Katherina_K.test_api_kkaplina.endpoints.delete_object import DeleteObject

url = 'https://api.restful-api.dev/objects'


@pytest.fixture()
def new_object_id():
    body = {
        "name": "NEW - Apple MacBook Pro 2024 Kate",
        "data": {
            "year": 2024,
            "price": 200,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        url,
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'{url}/{object_id}')


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
def delete_object():
    return DeleteObject()
