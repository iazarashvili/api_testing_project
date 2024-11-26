from config.base_api import BaseApi
from utils.helper import Helper
from utils.helpers.base_helpers import HelpFunctions
from utils.test_data.mercury_filters_beat_it import FiltersData


class TestCategories(BaseApi, Helper):

    def test_get_categories(self):
        response = self.mercury_filters_api.post_beat_it(FiltersData.post_beat_it_data())
        HelpFunctions.check_response_is_200(response)
        Helper.attach_response(self, response.json())
