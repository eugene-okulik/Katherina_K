TEST_DATA_CREATE_ACCOUNT = {
    "first_name": "Kate_123",
    "last_name": "Test_123",
    "email": "kate_123@test.test",
    "password": "123QWqw!",
    "confirm_password": "123QWqw!"
}

NEGATIVE_DATA_CREATE_ACCOUNT = [
    {
        'first_name': '',
        'last_name': 'Test_100',
        'email': 'kate_100@test.test',
        'password': '123QWqw!',
        'confirm_password': '123QWqw!'
    },
    {
        'first_name': 'Kate_100',
        'last_name': '',
        'email': 'kate_100@test.test',
        'password': '123QWqw!',
        'confirm_password': '123QWqw!'
    },
    {
        'first_name': 'Kate_100',
        'last_name': 'Test_100',
        'email': '',
        'password': '123QWqw!',
        'confirm_password': '123QWqw!'
    },
    {
        'first_name': 'Kate_100',
        'last_name': 'Test_100',
        'email': 'kate_100@test.test',
        'password': '',
        'confirm_password': '123QWqw!'
    },
    {
        'first_name': 'Kate_100',
        'last_name': 'Test_100',
        'email': 'kate_100@test.test',
        'password': '123QWqw!',
        'confirm_password': ''
    }
]
