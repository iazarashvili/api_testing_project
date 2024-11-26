import allure
import pytest

from utils.helpers.wishlist_helper import WishListHelpers
from config.base_api import BaseApi
from utils.helpers.base_helpers import HelpFunctions
from services.basket_service.basket_models.wish_list_schema import WishlistSchema


@allure.epic('Wish list tests')
class TestWishList(BaseApi):

    def test_empty_wish_list(self):
        WishListHelpers.empty_wishlist()

    @allure.title('Check empty wish list response')
    def test_check_empty_wishlist(self):
        response = self.basket_wish_list_api.get_product_ids()
        HelpFunctions.check_response_is_200(response)
        assert len(response.json()) == 0, 'wish list is not empty'

    @allure.title('Add item to wish list')
    @pytest.mark.parametrize('item_id', (369313, 709389))
    def test_add_one_item_wishlist(self, item_id):
        response = self.basket_wish_list_api.post_add_product(item_id)
        HelpFunctions.check_response_is_200(response)
        response_list = self.basket_wish_list_api.get_products()
        HelpFunctions.check_response_is_200(response_list)
        WishlistSchema(**response_list.json())
        WishListHelpers.empty_wishlist()

    @allure.title('Add two item to wish list')
    def test_add_two_item_wishlist(self):
        first_item = self.basket_wish_list_api.post_add_product(369313)
        HelpFunctions.check_response_is_200(first_item)
        second_item = self.basket_wish_list_api.post_add_product(709389)
        HelpFunctions.check_response_is_200(second_item)
        WishListHelpers.empty_wishlist()
