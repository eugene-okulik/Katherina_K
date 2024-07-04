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


@pytest.mark.parametrize('name', ['', '    ', '!@#$^'])
def test_add_object(test_info, name):
    print('\nbefore test')
    body = {
        "name": "Apple MacBook Pro 2024 Kate",
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
    assert response.status_code == 200
    assert response.json()['name'] == 'Apple MacBook Pro 2024 Kate'
    assert response.json()['data']['year'] == 2024
    assert response.json()['data']['price'] == 200
    assert response.json()['data']['CPU model'] == "Intel Core i9"
    assert response.json()['data']['Hard disk size'] == "1 TB"
    print('after test')


@pytest.mark.critical
def test_update_object(new_object_id):
    print('\nbefore test')
    body = {
        "name": "Apple MacBook Pro 2024 Kate - Last model",
        "data": {
            "year": 2025,
            "price": 2000,
            "CPU model": "Intel Core i9",
            "Hard disk size": "10 TB",
            "color": "white"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{new_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'Apple MacBook Pro 2024 Kate - Last model'
    assert response.json()['data']['year'] == 2025
    assert response.json()['data']['price'] == 2000
    assert response.json()['data']['CPU model'] == "Intel Core i9"
    assert response.json()['data']['Hard disk size'] == "10 TB"
    assert response.json()['data']['color'] == "white"
    print('after test')


@pytest.mark.medium
def test_partially_update_object(new_object_id):
    print('\nbefore test')
    body = {
        "data": {
            "year": 2030,
            "price": 20000,
            "CPU model": "Intel Core i9",
            "Hard disk size": "10 TB",
            "color": "gold"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_object_id}', 
        json=body,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'NEW - Apple MacBook Pro 2024 Kate', 'Not correct name'
    assert response.json()['data']['year'] == 2030, 'Not correct year'
    assert response.json()['data']['price'] == 20000, 'Not correct price'
    assert response.json()['data']['CPU model'] == "Intel Core i9", 'Not correct CPU model'
    assert response.json()['data']['Hard disk size'] == "10 TB", 'Not correct Hard disk size'
    assert response.json()['data']['color'] == "gold", 'Not correct color'
    print('after test')


def test_delete_object(new_object_id):
    print('\nbefore test')
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    print('after test')
