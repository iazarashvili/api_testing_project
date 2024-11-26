import allure
from config.base_api import BaseApi
from utils.helper import Helper
from utils.test_data.mercury_test_data import SearchData
from utils.helpers.base_helpers import HelpFunctions


@allure.epic('POST Search Mamma mia')
class TestSearchMammaMia(BaseApi, Helper):
    @allure.step('POST Mamma mia')
    def test_cool_cat(self):
        response = self.mercury_search_api.post_mamma_mia(SearchData.search_text('ტელეფონი'))
        HelpFunctions.check_response_is_200(response)
        assert response.json(), 'Response is empty'
        self.attach_response(response.json())
