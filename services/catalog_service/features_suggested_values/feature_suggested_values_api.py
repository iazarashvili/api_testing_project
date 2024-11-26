import requests
import allure

from services.catalog_service.features_suggested_values.feature_suggested_values_endpoints import \
    FeatureSuggestedValuesEndpoints
from config.headers import Headers


class FeatureSuggestedValuesApi:

    def __init__(self):
        super().__init__()
        self._endpoints = FeatureSuggestedValuesEndpoints()
        self._headers = Headers()

    @allure.step('GET feature suggested values category id features feature id')
    def get_feature_suggested_values_category_id_features_feature_id(self, category_id: int, feature_id: int, params):
        response = requests.get(
            url=self._endpoints.get_feature_suggested_values_category_id_feature_id(category_id, feature_id),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET feature suggested values id')
    def get_feature_suggested_values_id(self, feature_id):
        response = requests.get(
            url=self._endpoints.get_feature_suggested_values_id(feature_id),
            headers=self._headers.cms_token,
        )
        return response

    @allure.step('POST feature suggested values')
    def post_feature_suggested_values(self, payload):
        response = requests.post(
            url=self._endpoints.post_feature_suggested_values(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE feature suggested values')
    def delete_feature_suggested_values(self, params):
        response = requests.delete(
            url=self._endpoints.delete_feature_suggested_values(),
            params=params,
            headers=self._headers.web_token
        )
        return response

    @allure.step('PUT feature suggested values change status')
    def put_feature_suggested_values_change_status(self, payload):
        response = requests.put(
            url=self._endpoints.put_feature_suggested_values_change_status(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT feature suggested values change sort index')
    def put_feature_suggested_values_change_sort_index(self, payload):
        response = requests.put(
            url=self._endpoints.put_feature_suggested_values_change_sort_index(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT feature suggested values change feature suggested value')
    def put_feature_suggested_values_change_feature_suggested_value(self, payload):
        response = requests.put(
            url=self._endpoints.put_feature_suggested_values_change_feature_suggested_value(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
