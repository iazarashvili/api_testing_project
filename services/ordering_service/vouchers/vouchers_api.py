import requests
import allure

from services.ordering_service.vouchers.vouchers_endpoints import VouchersEndpoints
from config.headers import Headers


class VouchersApi:
    def __init__(self):
        super().__init__()
        self._endpoints = VouchersEndpoints()
        self._headers = Headers()

    def post_vouchers(self, payload):
        response = requests.post(
            url=self._endpoints.post_vouchers(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_validate(self, params):
        response = requests.get(
            url=self._endpoints.get_validate(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_details(self, params):
        response = requests.get(
            url=self._endpoints.get_details(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
