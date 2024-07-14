import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check status code')
    def check_status_code_is_correct(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Check name')
    def check_name_is_correct(self, name):
        assert self.json['name'] == name

    @allure.step('Check year')
    def check_year_is_correct(self, year):
        assert self.json['data']['year'] == year

    @allure.step('Check price')
    def check_price_is_correct(self, price):
        assert self.json['data']['price'] == price

    @allure.step('Check CPU model')
    def check_cpu_model_is_correct(self,  cpu_model):
        assert self.json['data']['CPU model'] == cpu_model

    @allure.step('Check Hard disk size')
    def check_hard_disk_size_is_correct(self, hard_disk_size):
        assert self.json['data']['Hard disk size'] == hard_disk_size

    @allure.step('Check color')
    def check_color_is_correct(self, color):
        assert self.json['data']['color'] == color
