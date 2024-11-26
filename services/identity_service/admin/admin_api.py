import requests
import allure

from services.identity_service.admin.admin_endpoints import AdminEndpoints
from config.headers import Headers


class AdminApi:
    def __init__(self):
        super().__init__()
        self._endpoints = AdminEndpoints()
        self._headers = Headers()

    @allure.step('POST legal update')
    def post_legal_update(self, payload):
        response = requests.post(
            url=self._endpoints.post_legal_update(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST legal reset password')
    def post_legal_reset_password(self, payload):
        response = requests.post(
            url=self._endpoints.post_legal_reset_password(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST user create')
    def post_user_create(self, payload):
        response = requests.post(
            url=self._endpoints.post_user_create(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST resend temporary password')
    def post_resend_temporary_password(self, payload):
        response = requests.post(
            url=self._endpoints.post_user_resend_temporary_password(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT user role update')
    def put_user_role_update(self, payload):
        response = requests.put(
            url=self._endpoints.put_user_role_update(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE user delete')
    def delete_user_delete(self, payload):
        response = requests.delete(
            url=self._endpoints.delete_user_delete(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET user employees')
    def get_user_employees(self, params):
        response = requests.get(
            url=self._endpoints.get_user_employees(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET user employees for profile')
    def get_user_employees_for_profile(self):
        response = requests.get(
            url=self._endpoints.get_user_employees_for_profile(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST create representative')
    def post_create_representative(self, payload):
        response = requests.post(
            url=self._endpoints.post_create_representative(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE remove representative')
    def delete_remove_representative(self, payload):
        response = requests.delete(
            url=self._endpoints.delete_remove_representative(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST user authorize')
    def post_user_authorize(self, payload):
        response = requests.post(
            url=self._endpoints.post_user_authorize(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE by admin')
    def delete_by_admin(self, params):
        response = requests.delete(
            url=self._endpoints.delete_by_admin(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET users deleted')
    def get_users_deleted(self, params):
        response = requests.get(
            url=self._endpoints.get_users_deleted(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
