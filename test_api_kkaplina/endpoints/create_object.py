import requests
import allure
from project.Katherina_K.test_api_kkaplina.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    @allure.step('create new object')
    def new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
