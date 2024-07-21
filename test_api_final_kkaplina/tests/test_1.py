import pytest
import allure
from .test_data import TEST_DATA_CREATE, NEGATIVE_DATA_CREATE, NEGATIVE_DATA_UPDATE, invalid_token, another_user_token


@allure.title('Create new meme')
@pytest.mark.parametrize('data', TEST_DATA_CREATE)
def test_add_meme(post_create_meme, data, token):
    post_create_meme.new_meme(data, token)
    post_create_meme.check_status_code_is_correct(status_code=200)
    post_create_meme.check_text_is_correct(data['text'])
    post_create_meme.check_url_is_correct(data['url'])
    post_create_meme.check_tags_is_correct(data['tags'])
    post_create_meme.check_info_is_correct(data['info'])


def test_add_meme_unauthorized(post_create_meme):
    data = {
        "text": "test",
        "url": "https://i.pinimg.com/474x/95/7d/ee/957dee125eeec88b8c4b2ba493d13182.jpg",
        "tags": ["test", "test", "test"],
        "info": {"test": ["test", "test"]}
    }
    post_create_meme.new_meme(data, invalid_token)
    post_create_meme.report_errors()
    post_create_meme.check_status_code_is_unauthorized(status_code=401)


@pytest.mark.parametrize('data', NEGATIVE_DATA_CREATE)
def test_add_meme_with_negative_data(post_create_meme, data, token):
    post_create_meme.new_meme(data, token)
    post_create_meme.check_status_code_is_bad_request(status_code=400)


def test_update_meme(new_meme_id, put_update_meme, token):
    data = {
        "id": new_meme_id,
        "text": "Updated - How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    }
    put_update_meme.make_changes_in_meme(new_meme_id, data, token)
    put_update_meme.check_status_code_is_correct(status_code=200)
    put_update_meme.check_text_is_correct(data['text'])
    put_update_meme.check_url_is_correct(data['url'])
    put_update_meme.check_tags_is_correct(data['tags'])
    put_update_meme.check_info_is_correct(data['info'])


def test_update_meme_unauthorized(put_update_meme):
    meme_id = 100
    data = {
        "id": 100,
        "text": "Updated - How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    }
    put_update_meme.make_changes_in_meme(meme_id, data, invalid_token)
    put_update_meme.report_errors()
    put_update_meme.check_status_code_is_unauthorized(status_code=401)


def test_update_meme_forbidden(put_update_meme):
    meme_id = 100
    data = {
        "id": 100,
        "text": "Updated - How to enter a password",
        "url": "https://i.pinimg.com/originals/80/33/80/8033801dc20c8e502ace19c9cb6469a8.jpg",
        "tags": ["updated - password", "updated - shrek"],
        "info": {"000": ["111", "222"]}
    }
    put_update_meme.make_changes_in_meme(meme_id, data, another_user_token)
    put_update_meme.report_errors()
    put_update_meme.check_status_code_is_forbidden(status_code=403)


@pytest.mark.parametrize('data', NEGATIVE_DATA_UPDATE)
def test_update_meme_with_negative_data(put_update_meme, new_meme_id, data, token):
    put_update_meme.make_changes_in_meme(new_meme_id, data, token)
    put_update_meme.check_status_code_is_bad_request(status_code=400)


def test_get_one_meme(new_meme_id, get_request_meme, token):
    response = get_request_meme.get_meme_by_id(new_meme_id, token)
    if response is not None:
        get_request_meme.check_status_code_is_correct(status_code=200)
        get_request_meme.check_id_is_correct(response['id'])
        get_request_meme.check_text_is_correct(response['text'])
        get_request_meme.check_url_is_correct(response['url'])
        get_request_meme.check_tags_is_correct(response['tags'])
        get_request_meme.check_info_is_correct(response['info'])


def test_get_one_meme_unauthorized(get_request_meme):
    meme_id = 100
    get_request_meme.get_meme_by_id(meme_id, invalid_token)
    get_request_meme.report_errors()
    get_request_meme.check_status_code_is_unauthorized(status_code=401)


def test_get_all_meme(get_request_all_memes, token):
    response = get_request_all_memes.get_all_memes(token)
    if response is not None:
        get_request_all_memes.check_status_code_is_correct(status_code=200)
        data_list = response.get('data', [])
        get_request_all_memes.check_response_is_list(data_list)
        for meme in data_list:
            get_request_all_memes.check_id_not_empty(meme)
            get_request_all_memes.check_text_not_empty(meme)
            get_request_all_memes.check_url_not_empty(meme)
            get_request_all_memes.check_tags_not_empty(meme)
            get_request_all_memes.check_info_not_empty(meme)


def test_get_all_meme_unauthorized(get_request_all_memes):
    get_request_all_memes.get_all_memes(invalid_token)
    get_request_all_memes.report_errors()
    get_request_all_memes.check_status_code_is_unauthorized(status_code=401)


def test_delete_meme(new_meme_id, delete_meme, token):
    delete_meme.delete_meme_by_id(new_meme_id, token)
    delete_meme.check_status_code_is_correct(status_code=200)


def test_delete_meme_unauthorized(delete_meme):
    meme_id = 100
    delete_meme.delete_meme_by_id(meme_id, invalid_token)
    delete_meme.report_errors()
    delete_meme.check_status_code_is_unauthorized(status_code=401)


def test_delete_meme_forbidden(delete_meme):
    meme_id = 100
    delete_meme.delete_meme_by_id(meme_id, another_user_token)
    delete_meme.report_errors()
    delete_meme.check_status_code_is_forbidden(status_code=403)
