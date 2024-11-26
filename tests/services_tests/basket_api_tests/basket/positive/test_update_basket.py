import allure
import pytest

from config.base_api import BaseApi
from utils.helpers.base_helpers import HelpFunctions
from utils.helper import Helper
from services.mercury_services.mercury_model.search_schema import ProductsSchema
from services.basket_service.basket_models.basket_schema import BasketSchema
from utils.helpers.basket_helper import BasketHelpers


@allure.epic('Basket Tests')
class TestBasket(BaseApi, Helper):

    @allure.title('Get basket info')
    def test_get_basket(self, empty_basket):
        response = self.basket_api.get_items_to_cart()
        HelpFunctions.check_response_is_200(response)
        self.attach_response(response.json())

    @allure.title('Post Update basket')
    @pytest.mark.parametrize('item_count', (1, 2, 3, 10))
    def test_post_update_basket(self, item_count, empty_basket):
        response_gimme = self.mercury_products_api.post_gimme([247991])
        HelpFunctions.check_response_is_200(response_gimme)

        response = self.basket_api.post_update_basket(247991, response_gimme.json()['data'][0], item_count)
        HelpFunctions.check_response_is_200(response)

        self.attach_response(response.json())
        model = BasketSchema(**response.json())
        BasketHelpers.check_item_count(item_count, model.data[0].productCount)

    @allure.title('Add two different item')
    def test_add_two_different_item(self, empty_basket):
        response_gimme = self.mercury_products_api.post_gimme([709306, 709196])
        schema = ProductsSchema(**response_gimme.json())
        post_first_response = self.basket_api.post_update_basket(schema.data[0].id, response_gimme.json()['data'][0], 1)
        HelpFunctions.check_response_is_200(post_first_response)

        self.attach_response(post_first_response.json())
        post_response = self.basket_api.post_update_basket(schema.data[1].id, response_gimme.json()['data'][1], 1)
        HelpFunctions.check_response_is_200(post_response)

        self.attach_response(post_response.json())
        basket_schema = BasketSchema(**post_response.json())

        first_product_id = basket_schema.data[0].productId
        second_product_id = basket_schema.data[1].productId
        BasketHelpers.check_value_not_equal_expected_value(first_product_id, second_product_id)
        self.basket_api.post_empty_basket()
