import allure
import requests

from services.catalog_service.mobile_categories.mobile_categories_endpoints import MobileCategoriesEndpoints
from config.headers import Headers


class MobileCategoriesApi:

    def __init__(self):
        super().__init__()
        self._endpoints = MobileCategoriesEndpoints()
        self._headers = Headers()

    @allure.step('GET mobile categories home screen categories')
    def get_home_screen_categories(self):
        response = requests.get(
            url=self._endpoints.get_home_screen_categories(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET mobile categories home screen sub categories')
    def get_home_screen_sub_categories(self, category_id):
        """
        :param category_id: int
        """
        response = requests.get(
            url=self._endpoints.get_home_screen_sub_categories(),
            params=category_id,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET mobile categories home screen special offers')
    def get_home_screen_special_offers(self, params):
        """
        :param params: pageNumber int, pageSize int
        """
        response = requests.get(
            url=self._endpoints.get_home_screen_special_offers(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
