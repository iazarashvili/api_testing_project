import requests
import allure

from services.identity_service.roles.endpoints import RolesEndpoints
from config.headers import Headers
from utils.helper import Helper
from services.identity_service.roles.models.roles_schema import RolesSchema


class RolesApi(Helper):

    def __init__(self):
        super().__init__()
        self._endpoints = RolesEndpoints()
        self._headers = Headers()

    @allure.step('GET roles')
    def get_roles(self):
        response = requests.get(
            url=self._endpoints.get_roles(),
            headers=self._headers.web_token
        )
        assert response.status_code == 200
        model = RolesSchema(**response.json())
        return model

    @allure.step('POST roles')
    def post_roles(self, payload):
        response = requests.post(
            url=self._endpoints.post_roles(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET roles name')
    def get_roles_name(self, name):
        response = requests.get(
            url=self._endpoints.get_roles_name(name),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE roles name')
    def delete_roles_name(self, name: str):
        response = requests.delete(
            url=self._endpoints.delete_name(name),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET roles name permission')
    def get_roles_name_permission(self, name):
        response = requests.get(
            url=self._endpoints.get_name_permission(name),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST roles name permission')
    def post_roles_name_permission(self, name: str, params):
        response = requests.post(
            url=self._endpoints.post_name_permission(name),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE roles name permission')
    def delete_roles_name_permission(self, name: str, params):
        response = requests.delete(
            url=self._endpoints.delete_name_permission(name),
            params=params,
            headers=self._headers.cms_token
        )
        return response
