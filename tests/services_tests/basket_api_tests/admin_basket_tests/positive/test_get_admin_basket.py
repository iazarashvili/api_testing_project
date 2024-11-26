import allure
from config.base_api import BaseApi
from utils.data.data import Data
from services.basket_service.basket_models.basket_schema import BasketSchema
from utils.helper import Helper
from utils.helpers.base_helpers import HelpFunctions


@allure.epic('GET Admin Basket Tests')
class TestGetAdminBasket(BaseApi, Helper):

    @allure.title('Get admin basket')
    def test_get_admin_basket(self, empty_admin_basket):
        response = self.basket_admin_basket_api.get_admin_basket(Data.user_gui_id)
        HelpFunctions.check_response_is_200(response)
        data = BasketSchema(**response.json())
        HelpFunctions.check_json_data_value(data.totalPrice, 0)
        HelpFunctions.check_json_data_value(data.quantityFailed, False)
        self.attach_response(response.json())
