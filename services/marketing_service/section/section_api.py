import requests
import allure

from services.marketing_service.section.section_endpoints import SectionEndpoints
from config.headers import Headers


class SectionApi:
    def __init__(self):
        super().__init__()
        self._endpoints = SectionEndpoints()
        self._headers = Headers()

    def post_create_section(self, payload):
        response = requests.post(
            url=self._endpoints.post_create_section(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_change_section(self, payload):
        response = requests.put(
            url=self._endpoints.put_change_section(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_sections(self):
        response = requests.get(
            url=self._endpoints.get_sections(),
            headers=self._headers.cms_token
        )
        return response

    def get_sections_admin(self, params):
        response = requests.get(
            url=self._endpoints.get_sections_admin(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def geet_section_details(self, params):
        response = requests.get(
            url=self._endpoints.get_section_details(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def post_section_upload_image(self, payload):
        response = requests.post(
            url=self._endpoints.post_upload_image(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_section_sort_index(self, payload):
        response = requests.put(
            url=self._endpoints.put_sort_index(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def delete_section_image(self, params):
        response = requests.delete(
            url=self._endpoints.delete_image(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def delete_section(self, params: int):
        response = requests.delete(
            url=self._endpoints.delete_section(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
