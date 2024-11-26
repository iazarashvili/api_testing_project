import requests
import allure
from services.catalog_service.merchants.merchants_endpoints import MerchantsEndpoints
from config.headers import Headers


class MerchantApi:

    def __init__(self):
        super().__init__()
        self._endpoints = MerchantsEndpoints()
        self._headers = Headers

    @allure.step('GET merchants user slug')
    def get_merchants_user_slug(self, user_slug: str):
        response = requests.get(
            url=self._endpoints.get_merchants_user_slug(user_slug),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET merchants slug details')
    def get_merchants_slug_details(self, slug: str):
        response = requests.get(
            url=self._endpoints.get_merchants_slug_details(slug),
            headers=self._headers.cms_token
        )
        return response
