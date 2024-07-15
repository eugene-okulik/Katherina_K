import requests
import allure
from test_api_kkaplina.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.step('delete object')
    def delete_object_by_id(self, new_object_id):
        self.response = requests.delete(f'{self.url}/{new_object_id}')
        return self.response
