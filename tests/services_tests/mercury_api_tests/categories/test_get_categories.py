from config.base_api import BaseApi
from utils.helper import Helper
from utils.helpers.base_helpers import HelpFunctions


class TestCategories(BaseApi, Helper):

    def test_get_categories(self):
        response = self.mercury_categories_api.get_categories()
        HelpFunctions.check_response_is_200(response)
        Helper.attach_response(self, response.json())
