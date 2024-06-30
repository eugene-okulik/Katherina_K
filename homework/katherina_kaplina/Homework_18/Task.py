import requests


def add_object():
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
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Apple MacBook Pro 2024 Kate', 'Not correct name'
    assert response.json()['data']['year'] == 2024, 'Not correct year'
    assert response.json()['data']['price'] == 200, 'Not correct price'
    assert response.json()['data']['CPU model'] == "Intel Core i9", 'Not correct CPU model'
    assert response.json()['data']['Hard disk size'] == "1 TB", 'Not correct Hard disk size'


add_object()


def new_object():
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
    return response.json()['id']


def clear(object_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')


def update_object():
    object_id = new_object()
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
        f'https://api.restful-api.dev/objects/{object_id}', 
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'Apple MacBook Pro 2024 Kate - Last model', 'Not correct name'
    assert response.json()['data']['year'] == 2025, 'Not correct year'
    assert response.json()['data']['price'] == 2000, 'Not correct price'
    assert response.json()['data']['CPU model'] == "Intel Core i9", 'Not correct CPU model'
    assert response.json()['data']['Hard disk size'] == "10 TB", 'Not correct Hard disk size'
    assert response.json()['data']['color'] == "white", 'Not correct color'
    clear(object_id)


update_object()


def partially_update_object():
    object_id = new_object()
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
        f'https://api.restful-api.dev/objects/{object_id}', 
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'NEW - Apple MacBook Pro 2024 Kate', 'Not correct name'
    assert response.json()['data']['year'] == 2030, 'Not correct year'
    assert response.json()['data']['price'] == 20000, 'Not correct price'
    assert response.json()['data']['CPU model'] == "Intel Core i9", 'Not correct CPU model'
    assert response.json()['data']['Hard disk size'] == "10 TB", 'Not correct Hard disk size'
    assert response.json()['data']['color'] == "gold", 'Not correct color'
    clear(object_id)


partially_update_object()


def delete_object():
    object_id = new_object()
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'


delete_object()
