import requests

from services.mercury_services.categories.categoryes_endpoints import CategoriesEndpoint
from config.headers import Headers


class MercuryCategoriesApi:

    def __init__(self):
        super().__init__()
        self._endpoints = CategoriesEndpoint()
        self._headers = Headers()

    def get_categories(self):
        response = requests.get(
            url=self._endpoints.get_categories(),
            headers=self._headers.cms_token
        )
        return response

    def get_categories_identifier(self, identifier: str):
        response = requests.get(
            url=self._endpoints.get_categories_identifier(identifier),
            headers=self._headers.cms_token
        )
        return response

    def get_categories_identifier_cheri_cheri(self, identifier: str):
        response = requests.get(
            url=self._endpoints.get_categories_identifier_cheri_cheri(identifier),
            headers=self._headers.cms_token
        )
        return response
