from config.base_api import BaseApi
from utils.helper import Helper
from utils.test_data.mercury_test_data import SearchData
from utils.helpers.base_helpers import HelpFunctions


class TestSearchGoGo(BaseApi, Helper):

    def test_search_go_go(self):
        response = self.mercury_search_api.post_search_go_go(SearchData.search_text('ტელეფონი'))
        HelpFunctions.check_response_is_200(response)
        assert response.json()[0] == 'ტელეფონი'
        self.attach_response(response.json())
