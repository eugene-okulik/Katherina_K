from test_api_kkaplina.endpoints.endpoint import Endpoint
import requests
import allure


class GetRequestObject(Endpoint):
    @allure.step('get object')
    def get_object(self, new_object_id):
        self.response = requests.get(f'{self.url}/{new_object_id}')
        self.json = self.response.json()
        return self.json
