import requests
import allure

from config.headers import Headers
from services.reporting_services.basket.basket_endpoints import BasketEndpoints


class BasketReporting:

    def __init__(self):
        super().__init__()
        self._endpoints = BasketEndpoints()
        self._headers = Headers()

    @allure.step('GET basket abandoned carts excel')
    def get_abandoned_carts_excel(self, params):
        """
        :param params:  From: datatime: To datatime
        """
        response = requests.get(
            url=self._endpoints.get_abandoned_carts_excel(),
            headers=self._headers.cms_token,
            params=params
        )
        return response

    @allure.step('GET basket wishlist products excel')
    def get_wishlist_products_excel(self, params):
        """
        :param params:  From: datatime: To datatime
        """
        response = requests.get(
            url=self._endpoints.get_wishlist_products_excel(),
            headers=self._headers.cms_token,
            params=params
        )
        return response
