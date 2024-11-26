import allure
import requests

from services.catalog_service.collector_hub.collector_hub_payloads import CollectorHubPayloads
from services.catalog_service.collector_hub.collector_hub_endpoints import CollectorHubEndpoints
from config.headers import Headers


class CollectorHubApi:

    def __init__(self):
        super().__init__()
        self._endpoints = CollectorHubEndpoints()
        self._headers = Headers()

    @allure.step('POST import products')
    def post_import_products(self, payload):
        response = requests.post(
            url=self._endpoints.post_import_products(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST import product assets')
    def post_import_product_assets(self, payload):
        response = requests.post(
            url=self._endpoints.post_import_product_assets(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST update product stock and prices')
    def post_update_product_stock_and_prices(self, payload):
        response = requests.post(
            url=self._endpoints.post_update_product_stock_and_price(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST remove expired products')
    def post_remove_expired_products(self, payload):
        response = requests.post(
            url=self._endpoints.post_remove_expired_products(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
