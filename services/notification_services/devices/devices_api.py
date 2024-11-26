import allure
import requests

from services.notification_services.devices.devices_endpoints import DevicesEndpoints
from config.headers import Headers


class DevicesApi:

    def __init__(self):
        super().__init__()
        self._endpoints = DevicesEndpoints()
        self._headers = Headers()

    @allure.step('POST register device')
    def post_register_device(self, payload):
        response = requests.post(
            url=self._endpoints.post_register_device(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST unregister device')
    def post_unregister_device(self, payload):
        response = requests.post(
            url=self._endpoints.post_unregister_device(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT change registration token')
    def put_change_registration_token(self, payload):
        response = requests.put(
            url=self._endpoints.put_change_registration_token(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST validate token')
    def post_validate_token(self, payload):
        response = requests.post(
            url=self._endpoints.post_validate_token(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST register apn token')
    def post_register_apn_token(self, payload):
        response = requests.post(
            url=self._endpoints.post_register_apns_token(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
