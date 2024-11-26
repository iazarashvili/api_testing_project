import allure

from config.base_api import BaseApi
from utils.helpers.base_helpers import HelpFunctions
from utils.helper import Helper
from services.basket_service.basket_models.basket_schema import BasketSchema
from utils.helpers.basket_helper import BasketHelpers


@allure.epic('Basket Tests')
class TestEmptyBasket(BaseApi, Helper):

    @allure.title('POST update basket products')
    def test_post_empty_basket(self, empty_basket):
        response = self.basket_api.post_update_basket_products(366636, 1)
        HelpFunctions.check_response_is_200(response)
        BasketSchema(**response.json())
        BasketHelpers.check_item_id(response, 366636)
