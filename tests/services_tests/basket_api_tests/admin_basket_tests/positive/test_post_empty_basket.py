import allure
from config.base_api import BaseApi
from utils.helper import Helper
from utils.data.data import Data
from services.basket_service.basket_models.basket_schema import BasketSchema
from utils.helpers.base_helpers import HelpFunctions


@allure.epic('POST admin basket remove product')
class TestEmptyBasket(BaseApi, Helper):

    @allure.step('POST admin basket empty basket')
    def test_empty_basket(self):
        response = self.basket_admin_basket_api.post_empty_basket(Data.user_gui_id)
        HelpFunctions.check_response_is_200(response)
        BasketSchema(**response.json())
        self.attach_response(response.json())
