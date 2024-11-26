import allure
import pytest

from config.base_api import BaseApi
from utils.helpers.base_helpers import HelpFunctions
from utils.helper import Helper
from services.mercury_services.mercury_model.search_schema import ProductsSchema
from services.basket_service.basket_models.basket_schema import BasketSchema
from utils.helpers.basket_helper import BasketHelpers


@allure.epic('GET basket')
class TestBasket(BaseApi, Helper):
    @allure.step('GET basket')
    def test_get_basket(self):
        response = self.basket_api.get_items_to_cart()
        HelpFunctions.check_response_is_200(response)
        BasketSchema(**response.json())
        self.attach_response(response.json())
