import requests
import allure

from services.identity_service.account.account_endpoints import AccountEndpoints
from config.headers import Headers


class AccountApi:
    def __init__(self):
        super().__init__()
        self._endpoints = AccountEndpoints()
        self._headers = Headers()

    @allure.step('GET External')
    def get_external(self, params):
        response = requests.get(
            url=self._endpoints.get_external(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET impersonate user')
    def get_impersonate_user(self, user_id: str):
        response = requests.get(
            url=self._endpoints.get_impersonate_user(),
            params=user_id,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET is impersonated user')
    def get_is_impersonated_user(self):
        response = requests.get(
            url=self._endpoints.get_is_impersonated_user(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET external login callback')
    def get_external_login_callback(self, params):
        response = requests.get(
            url=self._endpoints.get_external_login_call_back(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET sign out')
    def get_sign_out(self, params):
        """
        :param params: returnUrl: str
        """
        response = requests.get(
            url=self._endpoints.get_sign_out(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET exists username')
    def get_exists_username(self, user_name: str):
        response = requests.get(
            url=self._endpoints.get_exist_user_name(user_name),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST register')
    def post_register(self, payload):
        response = requests.post(
            url=self._endpoints.post_register(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST send verification')
    def post_send_verification(self, payload):
        response = requests.post(
            url=self._endpoints.post_send_verification(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST send password reset code')
    def post_send_password_reset_code(self, payload):
        response = requests.post(
            url=self._endpoints.post_send_password_reset_code(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST verify')
    def post_verify(self, payload):
        response = requests.post(
            url=self._endpoints.post_verify(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST set password')
    def post_set_password(self, payload):
        response = requests.post(
            url=self._endpoints.post_set_password(),
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
