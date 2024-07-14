import pytest

TEST_DATA = [
    {
        "name": "Apple MacBook Pro 2024 Kate",
        "data": {
            "year": 2024,
            "price": 200,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "HP 2024 Kate",
        "data": {
            "year": 2020,
            "price": 50,
            "CPU model": "Intel Core i9",
            "Hard disk size": "20 GB"
        }
    },
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_add_object(post_create_object, data):

    post_create_object.new_object(payload=data)
    post_create_object.check_status_code_is_correct(status_code=200)
    post_create_object.check_name_is_correct(data['name'])
    post_create_object.check_year_is_correct(data['data']['year'])
    post_create_object.check_price_is_correct(data['data']['price'])
    post_create_object.check_cpu_model_is_correct(data['data']['CPU model'])
    post_create_object.check_hard_disk_size_is_correct(data['data']['Hard disk size'])


def test_update_object(new_object_id, put_update_object):
    payload = {
        "name": "Apple MacBook Pro 2024 Kate - Last model",
        "data": {
            "year": 2025,
            "price": 2000,
            "CPU model": "Intel Core i9",
            "Hard disk size": "10 TB",
            "color": "white"
        }
    }

    put_update_object.make_changes_in_object(new_object_id, payload)
    put_update_object.check_status_code_is_correct(status_code=200)
    put_update_object.check_name_is_correct(payload['name'])
    put_update_object.check_year_is_correct(payload['data']['year'])
    put_update_object.check_price_is_correct(payload['data']['price'])
    put_update_object.check_cpu_model_is_correct(payload['data']['CPU model'])
    put_update_object.check_hard_disk_size_is_correct(payload['data']['Hard disk size'])
    put_update_object.check_color_is_correct(payload['data']['color'])


def test_partially_update_object(new_object_id, patch_update_object):

    payload = {
        "data": {
            "year": 2030,
            "price": 20000,
            "color": "gold"
        }
    }

    original_data = patch_update_object.get_object(new_object_id)
    patch_update_object.make_partial_changes_in_object(new_object_id, payload)
    patch_update_object.check_status_code_is_correct(status_code=200)
    patch_update_object.check_name_is_correct(original_data['name'])
    patch_update_object.check_year_is_correct(payload['data']['year'])
    patch_update_object.check_price_is_correct(payload['data']['price'])
    patch_update_object.check_cpu_model_is_correct(original_data['data']['CPU model'])
    patch_update_object.check_hard_disk_size_is_correct(original_data['data']['Hard disk size'])
    patch_update_object.check_color_is_correct(payload['data']['color'])


def test_delete_object(new_object_id, delete_object):
    delete_object.delete_object_by_id(new_object_id)
    delete_object.check_status_code_is_correct(status_code=200)
