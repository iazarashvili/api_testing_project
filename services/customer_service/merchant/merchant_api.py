import allure
import requests
from services.customer_service.merchant.merchant_endpoints import MerchantEndpoints
from config.headers import Headers


class MerchantApi:
    def __init__(self):
        super().__init__()
        self._endpoints = MerchantEndpoints()
        self._headers = Headers()

    def post_timeslot(self, payload):
        response = requests.post(
            url=self._endpoints.post_merchant_timeslot(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_cutoff_time(self, payload):
        response = requests.put(
            url=self._endpoints.put_merchant_cutoff_time(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_timeslot_details(self, params):
        response = requests.get(
            url=self._endpoints.get_merchant_timeslot_details(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
