from config.base_api import BaseApi
from utils.helper import Helper
from utils.helpers.base_helpers import HelpFunctions
from services.mercury_services.mercury_model.search_schema import ProductsSchema


class TestProducts(BaseApi, Helper):

    def test_post_gimme(self):
        response = self.mercury_products_api.post_gimme([709015])
        ProductsSchema(**response.json())
        print(response.json())
        HelpFunctions.check_response_is_200(response)
        Helper.attach_response(self, response.json())
