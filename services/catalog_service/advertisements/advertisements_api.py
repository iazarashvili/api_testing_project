import requests
import allure
from config.headers import Headers
from services.catalog_service.advertisements.advertisments_endpoints import AdvertisementsEndpoints
from services.catalog_service.advertisements.advertisements_params import AdvertisementsParams
from services.catalog_service.advertisements.advertiements_payloads import AdvertisementsPayload


class AdvertisementsApi:
    def __init__(self):
        super().__init__()
        self._endpoints = AdvertisementsEndpoints()
        self._params = AdvertisementsParams()
        self._payloads = AdvertisementsPayload()
        self._headers = Headers

    @allure.step('GET advertisements')
    def get_advertisements(self, page_number, page_size):
        response = requests.get(
            url=self._endpoints.get_advertisements,
            params=self._params.first_params(page_number, page_size),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST advertisements')
    def post_advertisements(self, payload):
        response = requests.post(
            url=self._endpoints.post_advertisements,
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT advertisements')
    def put_advertisements(self, payload):
        response = requests.post(
            url=self._endpoints.put_advertisements,
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE advertisements')
    def delete_advertisements(self, payload):
        response = requests.post(
            url=self._endpoints.delete_advertisements,
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET id')
    def get_id(self, id):
        response = requests.get(
            url=self._endpoints.get_id(id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET id categories')
    def get_id_categories(self, id):
        response = requests.get(
            url=self._endpoints.get_id_categories(id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET brand logos by category')
    def get_brand_logos_by_category(self, category_slug):
        response = requests.get(
            url=self._endpoints.get_brand_logos_by_category(category_slug),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST update categories')
    def post_update_categories(self, payload):
        response = requests.post(
            url=self._endpoints.post_update_categories,
            json=payload,
            headers=self._headers.cms_token
        )
        return response
