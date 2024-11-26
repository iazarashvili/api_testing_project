import requests
import allure

from services.payment_service.ipay.ipay_endpoints import IpayEndpoints
from config.headers import Headers


class IPayApi:
    def __init__(self):
        super().__init__()
        self._endpoints = IpayEndpoints()
        self._headers = Headers()

    @allure.step('POST payment')
    def post_payment(self, payloads):
        response = requests.post(
            url=self._endpoints.post_payment(),
            json=payloads,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST reversal')
    def post_reversal(self, payloads):
        response = requests.post(
            url=self._endpoints.post_reversal(),
            json=payloads,
            headers=self._headers.cms_token
        )
        return response
