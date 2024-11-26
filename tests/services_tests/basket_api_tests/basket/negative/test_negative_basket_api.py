import allure
from utils.helpers.base_helpers import HelpFunctions
from utils.helper import Helper
from config.base_api import BaseApi


class TestBasket(BaseApi, Helper):

    @allure.title('Add not existing item to cart')
    def test_update_basket_not_exist_item(self):
        self.basket_api.post_update_basket(89898089, 1, 0)

    @allure.title('Adding more than the existing quantity')
    def test_adding_more_than_existing_quantity(self):
        gimme_response = self.mercury_products_api.post_gimme([673581])
        item_json = gimme_response.json()['data'][0]
        self.basket_api.post_update_basket(673581, item_json, 21)

