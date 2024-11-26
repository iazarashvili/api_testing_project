import requests
import allure

from services.ordering_service.shipping_package_sizes.shipping_package_sizes_endpoints import ShippingPackageSizesEndpoints
from config.headers import Headers


class ShippingPackageSizesApi:
    def __init__(self):
        super().__init__()
        self._endpoints = ShippingPackageSizesEndpoints()
        self._headers = Headers()

    def post_shipping_package_size(self, payload):
        response = requests.post(
            url=self._endpoints.post_shipping_package_sizes(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_shipping_package_sizes(self, payload):
        response = requests.put(
            url=self._endpoints.put_shipping_package_sizes(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def delete_shipping_package_size(self, params):
        response = requests.delete(
            url=self._endpoints.delete_shipping_package_sizes(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_shipping_package_sizes(self):
        response = requests.get(
            url=self._endpoints.get_shipping_package_sizes(),
            headers=self._headers.cms_token
        )
        return response

    def get_shipping_package_sizes_id(self, package_size):
        response = requests.get(
            url=self._endpoints.get_shipping_package_sizes_id(package_size),
            params=package_size,
            headers=self._headers.cms_token
        )
        return response
