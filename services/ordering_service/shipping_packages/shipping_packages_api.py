import requests
import allure

from services.ordering_service.shipping_packages.shipping_packages_endpoints import ShippingPackagesEndpoints
from config.headers import Headers


class ShippingPackagesApi:

    def __init__(self):
        super().__init__()
        self._endpoints = ShippingPackagesEndpoints()
        self._headers = Headers()

    def post_shipping_packages(self, payload):
        response = requests.post(
            url=self._endpoints.post_shipping_packages(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_shipping_packages(self, payload):
        response = requests.put(
            url=self._endpoints.put_shipping_packages(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def delete_shipping_packages(self, params):
        response = requests.delete(
            url=self._endpoints.delete_shipping_packages(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_shipping_packages(self, params):
        response = requests.get(
            url=self._endpoints.get_shipping_packages(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def post_import_multiple(self, payload):
        response = requests.post(
            url=self._endpoints.post_import_multiple(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_change_activation(self, payload):
        response = requests.put(
            url=self._endpoints.put_change_activation(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_shipping_packages_id(self, package_id: int):
        response = requests.get(
            url=self._endpoints.get_shipping_package_id(package_id),
            headers=self._headers.cms_token
        )
        return response

    def get_import_template(self):
        response = requests.get(
            url=self._endpoints.get_import_template(),
            headers=self._headers.cms_token
        )
        return response
