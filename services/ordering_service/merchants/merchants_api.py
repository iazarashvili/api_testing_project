import requests
import allure

from services.ordering_service.merchants.merchants_endpoints import MerchantsEndpoints
from config.headers import Headers


class MerchantsApi:
    def __init__(self):
        super().__init__()
        self._endpoints = MerchantsEndpoints()
        self._headers = Headers()

    def post_sales(self, payload):
        response = requests.post(
            url=self._endpoints.post_sales(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_sales_averages(self, payload):
        response = requests.post(
            url=self._endpoints.post_sales_averages(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_sales_top_products(self, payload):
        response = requests.post(
            url=self._endpoints.post_sales_top_products(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_sales_locations(self, payload):
        response = requests.post(
            url=self._endpoints.post_sales_locations(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_sales_out_of_stock(self, payload):
        response = requests.post(
            url=self._endpoints.post_sales_out_of_stock(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_category_ranking(self, payload):
        response = requests.post(
            url=self._endpoints.post_sales_category_ranking(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_has_active_order(self, params):
        response = requests.get(
            url=self._endpoints.get_has_active_order(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
