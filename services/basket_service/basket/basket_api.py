import allure
import requests

from services.basket_service.basket.basket_endpoints import BasketEndpoints
from config.headers import Headers
from services.basket_service.basket.basket_payloads import BasketPayload


class BasketApi:

    def __init__(self):
        super().__init__()
        self.endpoints = BasketEndpoints()
        self.headers = Headers()
        self.payloads = BasketPayload()

    @allure.step('Get basket info')
    def get_items_to_cart(self):
        response = requests.get(
            url=self.endpoints.get_basket,
            headers=self.headers.web_token
        )
        return response

    @allure.step('Post update basket multiple')
    def post_update_basket_multiple(self):
        response = requests.post(
            url=self.endpoints.post_update_basket_multiple,
            json=self.payloads.update_basket_multiple_payload(),
            headers=self.headers.web_token
        )
        return response

    @allure.step('Post update basket')
    def post_update_basket(self, item_id: int, item_json, count, dark_store_id=0):
        response = requests.post(
            url=self.endpoints.post_update_basket(),
            json=self.payloads.update_basket_payload(item_id, item_json, count, dark_store_id),
            headers=self.headers.web_token
        )
        return response

    @allure.step('post Remove product')
    def post_remove_product(self, product_id, dark_store_id=0):
        response = requests.post(
            url=self.endpoints.post_remove_product,
            json=self.payloads.post_remove_product_payload(product_id, dark_store_id),
            headers=self.headers.web_token
        )
        return response

    @allure.step('Empty basket')
    def post_empty_basket(self, dark_store_id=0):
        response = requests.post(
            url=self.endpoints.post_empty_basket,
            json=self.payloads.post_empty_basket_payload(dark_store_id),
            headers=self.headers.web_token
        )
        return response

    @allure.step('Post update basket products')
    def post_update_basket_products(self, product_id, product_count):
        response = requests.post(
            url=self.endpoints.post_update_basket_products,
            json=self.payloads.post_update_basket_products(product_id, product_count),
            headers=self.headers.web_token
        )
        return response

    @allure.step('Post update basket express products')
    def post_update_basket_express_products(self, dark_store_id):
        response = requests.post(
            url=self.endpoints.post_update_basket_express_products,
            json=self.payloads.post_update_basket_express_products(dark_store_id),
            headers=self.headers.web_token
        )
        return response
