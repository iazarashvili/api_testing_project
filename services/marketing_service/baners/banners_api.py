import allure
import requests

from services.marketing_service.baners.banners_endpoints import BannersEndpoints
from config.headers import Headers


class BannersApi:
    def __init__(self):
        super().__init__()
        self._endpoints = BannersEndpoints()
        self._headers = Headers()

    @allure.step('POST Banners create banner place')
    def post_create_banner_place(self, payload):
        response = requests.post(
            url=self._endpoints.post_create_banner_place(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE Banners delete banner place')
    def delete_banner_place(self, params):
        response = requests.delete(
            url=self._endpoints.delete_delete_banner_place(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET Banners banner places')
    def get_banner_places(self, params):
        response = requests.get(
            url=self._endpoints.get_banner_places(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET Banners banner place details')
    def get_banner_place_details(self, params):
        response = requests.get(
            url=self._endpoints.get_banner_place_details(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST Banners add banner')
    def post_add_banner(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_banner(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST Banners change banner status')
    def post_change_banner_status(self, payload):
        response = requests.post(
            url=self._endpoints.post_change_banner_status(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT Banners update banner sort index')
    def put_update_banner_sort_index(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_banner_sort_index(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE Banners remove banner')
    def delete_remove_banner(self, params):
        response = requests.delete(
            url=self._endpoints.delete_remove_banner(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST Banners upload banner image')
    def post_upload_banner_image(self, payload):
        response = requests.post(
            url=self._endpoints.post_upload_banner_image(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET Banners ribbon')
    def get_ribbon(self):
        response = requests.get(
            url=self._endpoints.get_ribbon(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT Banners update banner')
    def put_update_banner(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_banner(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET Banners dynamic banner place')
    def get_dynamic_banner_place(self, params):
        response = requests.get(
            url=self._endpoints.get_dynamic_banner_place(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT Banners change banner place owner')
    def put_change_banner_place_owner(self, payload):
        response = requests.put(
            url=self._endpoints.put_change_banner_place_owner(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET Banners details')
    def get_details(self, params):
        response = requests.get(
            url=self._endpoints.get_details(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET Banners dynamic banner places')
    def get_dynamic_banner_places(self, params):
        response = requests.get(
            url=self._endpoints.get_dynamic_banner_places(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
