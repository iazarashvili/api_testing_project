import requests
import allure

from services.identity_service.profile.endpoints import ProfileEndpoints
from config.headers import Headers


class ProfileApi:
    def __init__(self):
        super().__init__()
        self._endpoints = ProfileEndpoints()
        self._headers = Headers()

    @allure.step('POST email send verification')
    def post_email_send_verification(self, payload):
        response = requests.post(
            url=self._endpoints.post_email_send_verification(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST phone send verification')
    def post_phone_send_verification(self, payload):
        response = requests.post(
            url=self._endpoints.phone_send_verification(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST change user name')
    def post_change_user_name(self, payload):
        response = requests.post(
            url=self._endpoints.post_change_user_name(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST change phone')
    def post_change_phone(self, payload):
        response = requests.post(
            url=self._endpoints.post_change_phone(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST change password')
    def post_change_password(self, payload):
        response = requests.post(
            url=self._endpoints.post_change_password(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST check password')
    def post_check_password(self, payload):
        response = requests.post(
            url=self._endpoints.post_check_password(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST send reset password token')
    def post_send_reset_password_token(self, payload):
        response = requests.post(
            url=self._endpoints.post_send_reset_password_token(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST reset password')
    def post_reset_password(self, payload):
        response = requests.post(
            url=self._endpoints.post_reset_password(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST delete')
    def post_delete(self):
        response = requests.post(
            url=self._endpoints.post_delete(),
            headers=self._headers.cms_token
        )
        return response
