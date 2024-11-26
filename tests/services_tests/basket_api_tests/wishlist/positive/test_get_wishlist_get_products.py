import allure
import pytest

from utils.helpers.wishlist_helper import WishListHelpers
from config.base_api import BaseApi
from utils.helpers.base_helpers import HelpFunctions
from services.basket_service.basket_models.wish_list_schema import WishlistSchema


@allure.epic('Wish list tests')
class TestGetWishListGetProducts(BaseApi):

    def test_empty_wish_list(self):
        WishListHelpers.empty_wishlist()

    @allure.title('GET wish list get products')
    def test_check_empty_wishlist(self):
        self.basket_wish_list_api.post_add_product(369313)
        response = self.basket_wish_list_api.get_products()
        HelpFunctions.check_response_is_200(response)
        WishlistSchema(**response.json())
