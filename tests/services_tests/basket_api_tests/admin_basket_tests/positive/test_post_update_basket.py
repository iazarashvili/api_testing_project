import allure

from config.base_api import BaseApi
from utils.helper import Helper
from utils.data.data import Data
from services.basket_service.basket_models.basket_schema import BasketSchema
from utils.helpers.base_helpers import HelpFunctions
from utils.data.basket_tests_data import BasketTestData
from utils.enums.global_messages import GlobalErrorMessages
from utils.helpers.basket_helper import BasketHelpers

product_id = BasketTestData.product_id
second_product_id = BasketTestData.second_product_id


@allure.epic('POST admin basket update basket')
class TestPostAdminBasketUpdateBasket(BaseApi, Helper):

    @allure.step('POST admin basket update basket')
    def test_admin_basket_update_basket(self, empty_admin_basket):
        response = self.basket_admin_basket_api.post_update_basket(Data.user_gui_id, product_id, 1)
        HelpFunctions.check_response_is_200(response)
        response_data = BasketSchema(**response.json())
        HelpFunctions.check_json_data_value(response_data.data[0].productId, product_id)
        assert response_data.data[0].productStatus == 1, 'Product is not active'
        assert response_data.data[0].productCount == 1, GlobalErrorMessages.WRONG_PRODUCT_COUNT.value
        self.attach_response(response.json())

    @allure.step('POST add item count 2 to admin basket')
    def test_add_item_to_basket_count_two(self, empty_admin_basket):
        response = self.basket_admin_basket_api.post_update_basket(Data.user_gui_id, product_id, 2)
        HelpFunctions.check_response_is_200(response)
        response_data = BasketSchema(**response.json())
        HelpFunctions.check_json_data_value(response_data.data[0].productId, product_id)
        assert response_data.data[0].productStatus == 1, 'Product is not active'
        assert response_data.data[0].productCount == 2, GlobalErrorMessages.WRONG_PRODUCT_COUNT.value
        self.attach_response(response.json())

    @allure.step('POST add two item to admin basket')
    def test_add_two_item_to_admin_basket(self, empty_admin_basket):
        first_response = self.basket_admin_basket_api.post_update_basket(Data.user_gui_id, product_id, 1)
        HelpFunctions.check_response_is_200(first_response)
        second_response = self.basket_admin_basket_api.post_update_basket(Data.user_gui_id, second_product_id, 1)
        HelpFunctions.check_response_is_200(second_response)
        response_data = BasketSchema(**second_response.json())
        self.attach_response(second_response.json())
        BasketHelpers.check_item_id(response_data.data[0].productId, second_product_id)
        BasketHelpers.check_item_id(response_data.data[1].productId, product_id)
