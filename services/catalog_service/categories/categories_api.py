import allure
import requests

from config.headers import Headers
from services.catalog_service.categories.categories_payloads import CategoriesPayloads
from services.catalog_service.categories.categories_endpoints import CategoriesEndpoints


class CategoriesApi:

    def __init__(self):
        super().__init__()
        self._endpoints = CategoriesEndpoints()
        self._payloads = CategoriesPayloads()
        self._headers = Headers()

    @allure.step('POST categories check node categories')
    def post_check_node_categories(self, category_ids: list):
        response = requests.post(
            url=self._endpoints.post_check_node_categories(),
            json=self._payloads.post_check_node_categories(category_ids),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET categories flat')
    def get_categories_flat(self):
        response = requests.get(
            url=self._endpoints.get_flat(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET categories as dictionary')
    def get_as_dictionary(self):
        response = requests.get(
            url=self._endpoints.get_as_dictionary(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET categories nested')
    def get_categories_nested(self):
        response = requests.get(
            url=self._endpoints.get_nested(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET categories last node categories')
    def get_last_node_categories(self, search_value: str, page_number: int, page_size: int):
        response = requests.get(
            url=self._endpoints.get_categories_last_node_categories(search_value, page_number, page_size),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET categories')
    def get_categories(self, input_string: str):
        response = requests.get(
            url=self._endpoints.get_categories(input_string),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST categories')
    def post_categories(self, payload):
        response = requests.post(
            url=self._endpoints.post_categories(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT categories')
    def put_categories(self, payloads):
        response = requests.put(
            url=self._endpoints.put_categories(),
            json=payloads,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET last node categories published')
    def get_last_node_categories_published(self, search_value: str, page_number: int, page_size: int):
        response = requests.get(
            url=self._endpoints.get_last_node_categories_published(search_value, page_number, page_size),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET categories id')
    def get_categories_id(self, category_id):
        response = requests.get(
            url=self._endpoints.get_categories_id(category_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET categories id features')
    def get_categories_id_features(self, category_id: int):
        response = requests.get(
            url=self._endpoints.get_categories_id_features(category_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET categories by-parent')
    def get_categories_by_parent(self, parent_id: int):
        response = requests.get(
            url=self._endpoints.get_by_parent(parent_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET categories id brands')
    def get_categories_id_brands(self, category_id: int):
        response = requests.get(
            url=self._endpoints.get_categories_id_brands(category_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET categories search')
    def get_categories_search(self, search_value: str):
        response = requests.get(
            url=self._endpoints.get_categories_search(search_value),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST categories add multiple')
    def post_categories_add_multiple(self):
        pass

    @allure.step('PUT categories hide')
    def put_categories_hide(self, payload):
        response = requests.put(
            url=self._endpoints.put_categories_hide(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST categories add feature')
    def post_add_feature(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_feature(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT categories update feature')
    def put_add_feature(self, payload):
        response = requests.post(
            url=self._endpoints.put_update_feature(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE categories remove feature')
    def delete_remove_feature(self, category_id: int, feature_id: int, correlation_id: str):
        response = requests.delete(
            url=self._endpoints.delete_remove_feature(category_id, feature_id, correlation_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT features change sort indexes')
    def put_features_change_sort_indexes(self, payload):
        response = requests.put(
            url=self._endpoints.def_put_features_change_sort_indexes(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response


