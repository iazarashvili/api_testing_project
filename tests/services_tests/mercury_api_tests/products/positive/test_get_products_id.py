from config.base_api import BaseApi
from utils.helper import Helper
from utils.helpers.base_helpers import HelpFunctions


class TestProducts(BaseApi, Helper):

    def test_get_product_id(self):
        response = self.mercury_products_api.get_products_id('709015')
        HelpFunctions.check_response_is_200(response)
        Helper.attach_response(self, response.json())
