import allure

from utils.helpers.wishlist_helper import WishListHelpers
from config.base_api import BaseApi
from utils.helpers.base_helpers import HelpFunctions


@allure.epic('Wish list tests')
class TestGetWishListProductIds(BaseApi):

    def test_empty_wish_list(self):
        WishListHelpers.empty_wishlist()

    @allure.title('GET wish list product ids')
    def test_get_wish_list_product_ids(self):
        self.basket_wish_list_api.post_add_product(709389)
        response = self.basket_wish_list_api.get_product_ids()
        HelpFunctions.check_response_is_200(response)
        assert response.json()[0] == 709389, 'Wish list is empty'
