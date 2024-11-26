import allure
from config.base_api import BaseApi
from utils.helper import Helper
from utils.test_data.mercury_test_data import SearchData
from utils.helpers.base_helpers import HelpFunctions


@allure.epic('POST Search sunny')
class TestSearchSunny(BaseApi, Helper):
    @allure.step('POST sunny')
    def test_cool_cat(self):
        response = self.mercury_search_api.post_sunny(SearchData.sunny())
        HelpFunctions.check_response_is_200(response)
        self.attach_response(response.json())
