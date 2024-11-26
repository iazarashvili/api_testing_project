import allure

from config.base_api import BaseApi
from utils.helpers.base_helpers import HelpFunctions
from utils.helper import Helper
from services.basket_service.basket_models.basket_schema import BasketSchema


@allure.epic('Basket empty basket')
class TestEmptyBasket(BaseApi, Helper):

    @allure.title('POST empty basket')
    def test_post_empty_basket(self, empty_basket):
        response = self.basket_api.post_empty_basket()
        HelpFunctions.check_response_is_200(response)
        BasketSchema(**response.json())
