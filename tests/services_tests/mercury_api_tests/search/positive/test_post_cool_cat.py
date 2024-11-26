import allure

from config.base_api import BaseApi
from utils.helper import Helper
from utils.test_data.mercury_test_data import SearchData
from utils.helpers.base_helpers import HelpFunctions


@allure.epic('POST Search cool cat')
class TestSearchCoolCat(BaseApi, Helper):
    @allure.step('POST cool cat')
    def test_cool_cat(self):
        response = self.mercury_search_api.post_cool_cat(SearchData.cool_cat('ტელეფონი'))
        HelpFunctions.check_response_is_200(response)
        assert response.json() is not None
        self.attach_response(response.json())
