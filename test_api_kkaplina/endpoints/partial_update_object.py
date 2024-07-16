from test_api_kkaplina.endpoints.endpoint import Endpoint
import requests
import allure


class PartialUpdateObject(Endpoint):
    @allure.step('partial update object')
    def make_partial_changes_in_object(self, new_object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{new_object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
