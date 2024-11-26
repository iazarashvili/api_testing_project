import requests
import allure

from services.payment_service.space.spec_endpoints import SpecEndpoints
from config.headers import Headers


class SpaceApi:
    def __init__(self):
        super().__init__()
        self._endpoints = SpecEndpoints()
        self._headers = Headers()

    def post_create_qr(self, payload):
        response = requests.post(
            url=self._endpoints.post_create_qr(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_check_status(self, params):
        """
        :param params: orderId: str:
        """
        response = requests.get(
            url=self._endpoints.get_check_status(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def post_status_update(self, payload):
        response = requests.post(
            url=self._endpoints.post_status_update(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
