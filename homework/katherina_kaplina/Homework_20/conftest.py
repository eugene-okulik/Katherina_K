import requests
import pytest


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
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'https://api.restful-api.dev/objects/{object_id}')


@pytest.fixture(scope='session')
def test_info():
    print('Starting testing')
    yield
    print('Testing completed')