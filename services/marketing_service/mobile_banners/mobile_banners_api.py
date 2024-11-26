import allure
import requests

from services.marketing_service.mobile_banners.mobile_banners_endpoints import MobileBannersEndpoints
from config.headers import Headers


class MobileBannersApi:
    def __init__(self):
        super().__init__()
        self._endpoints = MobileBannersEndpoints()
        self._headers = Headers()

    def get_mobile_banners(self):
        response = requests.get(
            url=self._endpoints.get_mobile_banners(),
            headers=self._headers.cms_token
        )
        return response

    def get_landing_banners(self):
        response = requests.get(
            url=self._endpoints.get_mobile_banners_landing_banners(),
            headers=self._headers.cms_token
        )
        return response

    def get_advertisement_banners(self):
        response = requests.get(
            url=self._endpoints.get_mobile_banners_advertisement_banners(),
            headers=self._headers.cms_token
        )
        return response
