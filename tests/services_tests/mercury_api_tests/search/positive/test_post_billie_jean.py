from config.base_api import BaseApi
from utils.helper import Helper
from utils.test_data.mercury_test_data import SearchData
from utils.helpers.base_helpers import HelpFunctions


class TestSearchBillieJean(BaseApi, Helper):

    def test_search_billie_jean(self):
        response = self.mercury_search_api.post_search_billie_jean(SearchData.search_billie_jane('telefoni'))
        HelpFunctions.check_response_is_200(response)
        assert response.json() is not None
