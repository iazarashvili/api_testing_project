import allure

from config.base_api import BaseApi
from services.basket_service.basket_models.basket_schema import BasketSchema
from utils.data.basket_tests_data import BasketTestData
from utils.helper import Helper
from utils.helpers.base_helpers import HelpFunctions
from utils.data.data import Data

product_id = BasketTestData.product_id


@allure.epic('POST admin basket remove product')
class TestRemoveProduct(BaseApi, Helper):

    @allure.step('POST admin basket remove product')
    def test_admin_basket_remove_product(self, empty_admin_basket):
        self.basket_admin_basket_api.post_update_basket(Data.user_gui_id, product_id, 1)
        response = self.basket_admin_basket_api.post_remove_product(Data.user_gui_id, product_id)
        HelpFunctions.check_response_is_200(response)
        basket_data = BasketSchema(**response.json())
        assert basket_data.quantityFailed is False
        assert basket_data.totalPrice == 0
        self.attach_response(response.json())
