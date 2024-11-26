import allure
import requests

from services.catalog_service.brands.brands_payloads import BrandsPayload
from services.catalog_service.brands.brands_endpoints import BrandsEndpoints
from config.headers import Headers


class BrandApi:

    def __int__(self):
        super().__init__()
        self._payloads = BrandsPayload()
        self._endpoints = BrandsEndpoints()
        self._headers = Headers()
        self._web_headers = Headers()

    @allure.step('GET brands')
    def get_brands(self, search_value: str, page_number: int, page_size: int):
        response = requests.get(
            url=self._endpoints.get_brands(search_value, page_number, page_size),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST brands')
    def post_brands(self, payloads):
        response = requests.post(
            url=self._endpoints.post_brands,
            json=payloads,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT brands')
    def put_brands(self):
        response = requests.put(
            url=self._endpoints.put_brands,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE brands')
    def delete_brands(self, brand_id: int, correlation_id: str):
        response = requests.delete(
            url=self._endpoints.delete_brands(brand_id, correlation_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET brands brand id feature values')
    def get_brand_id_feature_values(self, brand_id):
        response = requests.get(
            url=self._endpoints.get_brand_id_feature_values(brand_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET brand id categories category id models')
    def get_brand_id_categories_category_id_models(self, brand_id: int, category_id: int, status: int):
        response = requests.get(
            url=self._endpoints.get_brand_id_categories_category_id_models(brand_id, category_id, status),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET brands by category id category id')
    def get_get_brands_by_category_id_category_id(self, category_id: int):
        response = requests.get(
            url=self._endpoints.get_brands_by_category_id_category_id(category_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET models by brand id, brand id category id')
    def get_models_by_brand_id_brand_id_category_id(self, brand_id: int, category_id: int):
        response = requests.get(
            url=self._endpoints.get_models_by_brand_id_brand_id_category_id(brand_id, category_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET brands brand id categories')
    def get_brand_id_categories(self, brand_id: int):
        response = requests.get(
            url=self._endpoints.get_brand_id_categories(brand_id),
            headers=self._headers.web_token
        )
        return response

    @allure.step('GET brands, brand id')
    def get_brand_id(self, brand_id: int):
        response = requests.get(
            url=self._endpoints.get_brands_id(brand_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST brands add category')
    def post_add_category(self):
        response = requests.post(
            url=self._endpoints.post_add_category(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE brands remove category')
    def delete_brands_remove_category(self, brand_id: int, category_id: int, correlation_id: int):
        response = requests.delete(
            url=self._endpoints.delete_remove_category(brand_id, category_id, correlation_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST brands add category feature value')
    def post_brands_add_category_feature_value(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_category_feature_value(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT brands update category feature values')
    def put_update_category_feature_value(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_category_feature_value(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE remove category feature value')
    def delete_remove_category_feature_value(self, feature_suggested_value_id: int, correlation_id: int):
        response = requests.delete(
            url=self._endpoints.delete_remove_category_feature_value(feature_suggested_value_id, correlation_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST brands add catalog-models')
    def post_add_model(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_model(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT brands update catalog-models')
    def put_update_model(self, payload):
        response = requests.post(
            url=self._endpoints.put_update_model(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE brands remove catalog-models')
    def delete_remove_model(self, brand_category_id: int, model_id, correlation_id: int):
        response = requests.post(
            url=self._endpoints.delete_remove_model(brand_category_id, model_id, correlation_id),
            headers=self._headers.cms_token
        )
        return response
