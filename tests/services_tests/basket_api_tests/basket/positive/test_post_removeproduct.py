import allure
import pytest

from config.base_api import BaseApi
from utils.helpers.base_helpers import HelpFunctions
from utils.helper import Helper
from services.mercury_services.mercury_model.search_schema import ProductsSchema
from services.basket_service.basket_models.basket_schema import BasketSchema
from utils.helpers.basket_helper import BasketHelpers


@allure.epic('Basket Tests')
class TestRemoveProduct(BaseApi, Helper):

    @allure.title('Remove one product from the cart')
    def test_remove_product_from_cart(self, empty_basket):
        response_gimme = self.mercury_products_api.post_gimme([709306, 709196])
        schema = ProductsSchema(**response_gimme.json())
        self.basket_api.post_update_basket(schema.data[0].id, response_gimme.json()['data'][0], 1)
        post_response = self.basket_api.post_update_basket(schema.data[1].id, response_gimme.json()['data'][1], 1)
        data = BasketSchema(**post_response.json())
        self.basket_api.post_remove_product(data.data[0].productId)
