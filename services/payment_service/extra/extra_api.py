import requests
import allure

from services.payment_service.extra.extra_endpoints import ExtraEndpoints
from config.headers import Headers


class ExtraApi:
    def __init__(self):
        super().__init__()
        self._endpoints = ExtraEndpoints()
        self._headers = Headers()

    def post_add_balance_from_extra(self, payloads):
        response = requests.post(
            url=self._endpoints.post_add_balance_from_extra(),
            json=payloads,
            headers=self._headers.cms_token
        )
        return response

    def post_remove_balance_from_extra(self, payload):
        response = requests.post(
            url=self._endpoints.post_remove_balance_from_extra(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_balance_transactions(self, params):
        response = requests.get(
            url=self._endpoints.get_balance_transactions(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_order_payment_details(self, params):
        response = requests.get(
            url=self._endpoints.get_order_payment_details(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def post_use_voucher(self, payload):
        response = requests.post(
            url=self._endpoints.post_use_voucher(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_order_refund_details(self, params):
        response = requests.get(
            url=self._endpoints.get_order_refund_details(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
