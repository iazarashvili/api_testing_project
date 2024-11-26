import requests
import allure
from services.basket_service.admin_basket.admin_basket_payloads import AdminBasketPayloads
from services.basket_service.admin_basket.admin_basket_endpoints import AdminBasketEndpoints
from config.headers import Headers
from utils.helper import Helper


class AdminBasketApi(Helper):

    def __init__(self):
        super().__init__()
        self._endpoints = AdminBasketEndpoints()
        self._headers = Headers()
        self._payload = AdminBasketPayloads()

    @allure.step('GET admin basket')
    def get_admin_basket(self, user_gui_id: str, dark_store_id=0):
        response = requests.get(
            url=self._endpoints.get_admin_basket(user_gui_id, dark_store_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST update basket')
    def post_update_basket(self, user_gui_id: str, product_id, product_count, dark_store_id=0):
        response = requests.post(
            url=self._endpoints.post_update_basket(user_gui_id, dark_store_id),
            json=self._payload.post_update_basket(product_id, product_count),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST remove product')
    def post_remove_product(self, user_gui_id: str, product_id: int, dark_store_id=0):
        response = requests.post(
            url=self._endpoints.post_remove_product(user_gui_id, dark_store_id),
            json=self._payload.post_remove_products(product_id, dark_store_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST empty basket')
    def post_empty_basket(self, user_gui_id, dark_store_id=0):
        response = requests.post(
            url=self._endpoints.post_empty_basket(user_gui_id, dark_store_id),
            headers=self._headers.cms_token
        )
        return response
