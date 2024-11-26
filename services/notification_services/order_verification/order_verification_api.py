import allure
import requests

from services.notification_services.order_verification.order_verification_endpoints import OrderVerificationEndpoints
from config.headers import Headers


class OrderVerification:
    def __init__(self):
        super().__init__()
        self._endpoints = OrderVerificationEndpoints()
        self._headers = Headers()

    @allure.step('GET order verification otp')
    def get_order_verification_otp(self, params):
        response = requests.get(
            url=self._endpoints.get_order_verification_otp(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT order verification verify')
    def put_order_verification_verify(self, payload):
        response = requests.put(
            url=self._endpoints.put_order_verification_verify(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
