import allure
import requests

from services.marketing_service.landing_pages.landing_pages_endpoints import LandingPagesEndpoints
from config.headers import Headers


class LandingPagesApi:
    def __init__(self):
        super().__init__()
        self._endpoints = LandingPagesEndpoints()
        self._headers = Headers()

    def get_landing_pages(self, params):
        response = requests.get(
            url=self._endpoints.get_landing_pages(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def post_landing_pages(self, payload):
        response = requests.post(
            url=self._endpoints.post_landing_pages(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_landing_pages(self, payload):
        response = requests.put(
            url=self._endpoints.put_landing_pages(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def delete_landing_pages(self, payload):
        response = requests.delete(
            url=self._endpoints.delete_landing_pages(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_landing_pages_id(self, any_id: int):
        response = requests.get(
            url=self._endpoints.get_landing_pages_id(any_id),
            headers=self._headers.cms_token
        )
        return response

    def get_landing_pages_id_products(self, product_id: int, params):
        response = requests.get(
            url=self._endpoints.get_id_products(product_id),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_landing_pages_by_slug_slug(self, slug: str):
        response = requests.get(
            url=self._endpoints.get_by_slug_slug(slug),
            headers=self._headers.cms_token
        )
        return response

    def post_landing_pages_id_products_add(self, page_id: int, payload):
        response = requests.post(
            url=self._endpoints.post_id_products_add(page_id),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_landing_pages_id_products_remove(self, page_id: int, payload):
        response = requests.post(
            url=self._endpoints.post_id_products_remove(page_id),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_landing_pages_id_products_import(self, page_id: int, payload):
        response = requests.post(
            url=self._endpoints.post_id_products_import(page_id),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
