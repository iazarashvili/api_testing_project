import requests
import allure

from services.payment_service.installments.installments_endpoints import InstallmentsEndpoints
from config.headers import Headers


class InstallmentsApi:
    def __init__(self):
        super().__init__()
        self._endpoints = InstallmentsEndpoints()
        self._headers = Headers()

    @allure.step('POST installments')
    def post_installments(self, payload):
        response = requests.post(
            url=self._endpoints.post_installments(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET ipay check status')
    def get_ipay_check_status(self, params):
        response = requests.get(
            url=self._endpoints.get_ipay_check_status(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET tbc check status')
    def get_tbc_check_status(self, params):
        response = requests.get(
            url=self._endpoints.get_tbc_check_status(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
