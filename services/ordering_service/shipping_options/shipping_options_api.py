import requests
import allure

from services.ordering_service.shipping_options.shipping_options_endpoints import ShippingOptionsEndpoints
from config.headers import Headers


class ShippingOptionsApi:
    def __init__(self):
        super().__init__()
        self._endpoints = ShippingOptionsEndpoints()
        self._headers = Headers()

    def post_shipping_options(self, payload):
        response = requests.post(
            url=self._endpoints.post_shipping_options(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_shipping_options(self, payload):
        response = requests.put(
            url=self._endpoints.put_shipping_options(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_shipping_options(self, params):
        response = requests.get(
            url=self._endpoints.get_shipping_options(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def patch_shipping_options_id_status(self, shipping_option_id: int, payload=1):
        response = requests.patch(
            url=self._endpoints.patch_id_status(shipping_option_id),
            headers=self._headers.cms_token,
            json=payload
        )
        return response

    def delete_shipping_options_id(self, shipping_options_id: int):
        response = requests.delete(
            url=self._endpoints.delete_shipping_options_id(shipping_options_id),
            headers=self._headers.cms_token
        )
        return response

    def get_shipping_options_id(self, shipping_options_id: int):
        response = requests.get(
            url=self._endpoints.get_shipping_options_id(shipping_options_id),
            headers=self._headers.cms_token
        )
        return response
