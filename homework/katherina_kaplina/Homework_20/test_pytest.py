import requests
import pytest
import allure


@allure.feature('Add object')
@allure.story('Store #5 Laptop')
@allure.title('Add object')
@allure.description('This case is needed for the next release')
@pytest.mark.parametrize('name', ['', '    ', '!@#$^'])
def test_add_object(test_info, name):
    print('\nbefore test')
    with allure.step('Prepare test data'):
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
    with allure.step('Run POST request to add new object'):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            json=body,
            headers=headers
        )
    with allure.step('Check status code is 200'):
        assert response.status_code == 200
    with allure.step('Check name'):
        assert response.json()['name'] == 'Apple MacBook Pro 2024 Kate'
    with allure.step('Check year'):
        assert response.json()['data']['year'] == 2024
    with allure.step('Check price'):
        assert response.json()['data']['price'] == 200
    with allure.step('Check CPU model'):
        assert response.json()['data']['CPU model'] == "Intel Core i9"
    with allure.step('Check Hard disk size'):
        assert response.json()['data']['Hard disk size'] == "1 TB"
    print('after test')


@allure.feature('Update object')
@allure.story('Store #5 Laptop')
@allure.title('Update object')
@allure.description('This case is needed for UPCOMING release')
@allure.issue('https:///api.restful-api.dev/objects', 'KATE-13')
@pytest.mark.critical
def test_update_object(new_object_id):
    print('\nbefore test')
    with allure.step('Prepare test data'):
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
    with allure.step('Run PUT request to update object'):
        response = requests.put(
            f'https://api.restful-api.dev/objects/{new_object_id}',
            json=body,
            headers=headers
        )
    with allure.step('Check status code is 200'):
        assert response.status_code == 200
    with allure.step('Check name'):
        assert response.json()['name'] == 'Apple MacBook Pro 2024 Kate - Last model'
    with allure.step('Check year'):
        assert response.json()['data']['year'] == 2025
    with allure.step('Check price'):
        assert response.json()['data']['price'] == 2000
    with allure.step('Check CPU model'):
        assert response.json()['data']['CPU model'] == "Intel Core i9"
    with allure.step('Check Hard disk size'):
        assert response.json()['data']['Hard disk size'] == "10 TB"
    with allure.step('Check color'):
        assert response.json()['data']['color'] == "white"
    print('after test')


@allure.feature('Update object')
@allure.story('Store #5 Laptop')
@allure.title('Partial update object')
@allure.description('This case is needed for UPCOMING release')
@pytest.mark.medium
def test_partially_update_object(new_object_id):
    print('\nbefore test')
    with allure.step('Prepare test data'):
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
    with allure.step('Run PATCH request to update object'):
        response = requests.patch(
            f'https://api.restful-api.dev/objects/{new_object_id}',
            json=body,
            headers=headers
        )
    with allure.step('Check status code is 200'):
        assert response.status_code == 200
    with allure.step('Check name'):
        assert response.json()['name'] == 'NEW - Apple MacBook Pro 2024 Kate', 'Not correct name'
    with allure.step('Check year'):
        assert response.json()['data']['year'] == 2030, 'Not correct year'
    with allure.step('Check price'):
        assert response.json()['data']['price'] == 20000, 'Not correct price'
    with allure.step('Check CPU model'):
        assert response.json()['data']['CPU model'] == "Intel Core i9", 'Not correct CPU model'
    with allure.step('Check Hard disk size'):
        assert response.json()['data']['Hard disk size'] == "10 TB", 'Not correct Hard disk size'
    with allure.step('Check color'):
        assert response.json()['data']['color'] == "gold", 'Not correct color'
    print('after test')


@allure.feature('Delete object')
@allure.story('Store #6 Mobile phone')
@allure.title('Delete object')
@allure.description('This case is needed for the next release')
def test_delete_object(new_object_id):
    print('\nbefore test')
    with allure.step('Run DELETE request to delete object'):
        response = requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')
    with allure.step('Check status code is 200'):
        assert response.status_code == 200, 'Status code is incorrect'
    print('after test')
