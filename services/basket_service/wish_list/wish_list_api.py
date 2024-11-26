import allure
import requests

from services.basket_service.wish_list.wish_list_endpoints import WishListEndpoints
from services.basket_service.wish_list.wish_list_payloads import WishListPayload
from utils.helper import Helper
from config.headers import Headers


class WishListApi(Helper):

    def __init__(self):
        super().__init__()
        self.endpoints = WishListEndpoints()
        self._payload = WishListPayload()
        self._headers = Headers()

    @allure.step('POST add product')
    def post_add_product(self, product_id):
        response = requests.post(
            url=self.endpoints.post_add_product(),
            json=self._payload.post_add_product(product_id),
            headers=self._headers.web_token
        )
        return response

    @allure.step('GET get products')
    def get_products(self):
        response = requests.get(
            url=self.endpoints.get_products(),
            headers=self._headers.web_token
        )
        return response

    @allure.step('DELETE: remove product')
    def delete_remove_product(self, product_id):
        response = requests.delete(
            url=self.endpoints.delete_remove_product(product_id),
            headers=self._headers.web_token
        )
        return response

    @allure.step('GET product ids')
    def get_product_ids(self):
        response = requests.get(
            url=self.endpoints.get_product_ids,
            headers=self._headers.web_token
        )
        return response
