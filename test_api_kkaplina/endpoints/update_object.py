from test_api_kkaplina.endpoints.endpoint import Endpoint
import requests
import allure


class UpdateObject(Endpoint):
    @allure.step('update object')
    def make_changes_in_object(self, new_object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{new_object_id}',
            json=payload,
            headers=headers
        )
        # print(f'Response Status Code: {self.response.status_code}')
        # print(f'Response Body: {self.response.text}')
        self.json = self.response.json()
        return self.response
