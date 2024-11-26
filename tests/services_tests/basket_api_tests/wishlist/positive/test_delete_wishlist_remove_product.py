import allure

from utils.helpers.wishlist_helper import WishListHelpers
from config.base_api import BaseApi
from utils.helpers.base_helpers import HelpFunctions
from services.basket_service.basket_models.wish_list_schema import WishlistSchema


@allure.epic('DELETE wish list remove products')
class TestDeleteRemoveProduct(BaseApi):

    def test_empty_wish_list(self):
        WishListHelpers.empty_wishlist()

    @allure.title('DELETE wish list remove product')
    def test_check_empty_wishlist(self):
        self.basket_wish_list_api.post_add_product(369313)
        response = self.basket_wish_list_api.delete_remove_product(369313)
        HelpFunctions.check_response_is_200(response)
