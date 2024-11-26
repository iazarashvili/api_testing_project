import requests
import allure

from services.marketing_service.static_pages.static_pages_endpoints import StaticPagesEndpoints
from config.headers import Headers


class StaticPagesApi:
    def __init__(self):
        super().__init__()
        self._endpoints = StaticPagesEndpoints()
        self._headers = Headers()

    @allure.step('POST create static page')
    def post_create_static_page(self, payload):
        response = requests.post(
            url=self._endpoints.post_create_static_page(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('')
    def delete_remove_static_page(self, params):
        response = requests.delete(
            url=self._endpoints.delete_remove_static_page(),
            headers=self._headers.cms_token,
            params=params
        )
        return response

    @allure.step('')
    def get_static_pages(self, params):
        response = requests.get(
            url=self._endpoints.get_static_pages(),
            headers=self._headers.cms_token,
            params=params
        )
        return response

    @allure.step('')
    def put_update_static_page(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_static_page(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('')
    def get_static_page_details(self, params):
        response = requests.get(
            url=self._endpoints.get_static_page_details(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('')
    def post_create_static_page_group(self, payload):
        response = requests.post(
            url=self._endpoints.post_create_static_page_group(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('')
    def delete_remove_static_page_group(self, params):
        response = requests.delete(
            url=self._endpoints.delete_remove_static_page_group(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('')
    def get_static_page_groups(self, params):
        response = requests.get(
            url=self._endpoints.get_remove_static_page_group(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('')
    def get_static_page_groups_for_drop_down(self, params):
        response = requests.get(
            url=self._endpoints.get_static_page_groups_for_dropdown(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('')
    def put_update_static_page_group(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_static_page_group(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('')
    def get_static_page_group_details(self, params):
        response = requests.get(
            url=self._endpoints.get_static_page_group_details(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('')
    def get_static_page_and_groups(self):
        response = requests.get(
            url=self._endpoints.get_static_pages_and_groups(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('')
    def get_static_page_description(self, params):
        """
        :param params: url: str
        """
        response = requests.get(
            url=self._endpoints.get_static_page_description(),
            headers=self._headers.cms_token,
            params=params
        )
        return response
