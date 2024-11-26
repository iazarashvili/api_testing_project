import requests
import allure
from services.catalog_service.feature_group.feature_group_endpoints import FeatureGroupEndpoint
from config.headers import Headers


class FeatureGroupApi:

    def __init__(self):
        super().__init__()
        self._endpoint = FeatureGroupEndpoint()
        self._header = Headers()

    @allure.step('GET feature group')
    def get_feature_group(self, params):
        response = requests.get(
            url=self._endpoint.get_feature_group(),
            params=params,
            headers=self._header.web_token
        )
        return response

    @allure.step('POST feature group')
    def post_feature_group(self, payload):
        """
        :payload: correlationId, str: caption: str:
        """
        response = requests.post(
            url=self._endpoint.post_feature_group(),
            json=payload,
            headers=self._header.cms_token
        )
        return response

    @allure.step('PUT feature group')
    def put_feature_group(self, payload):
        """
        :payload: correlationId: str: id: int: caption: str:
        """
        response = requests.put(
            url=self._endpoint.put_feature_group(),
            json=payload,
            headers=self._header.cms_token

        )
        return response

    @allure.step('DELETE feature group')
    def delete_feature_group(self, params):
        """
        :param: id: int: CorrelationId: str: requestId: uuid:
        """
        response = requests.delete(
            url=self._endpoint.delete_feature_group(),
            params=params,
            headers=self._header.cms_token
        )
        return response

    @allure.step('GET feature group id')
    def get_feature_group_id(self, params):
        """
        :parameter: id: int:
        """
        response = requests.get(
            url=self._endpoint.get_feature_group_id(),
            params=params,
            headers=self._header.cms_token
        )
        return response

    @allure.step('PUT feature group change sort indexes')
    def put_feature_group_change_sort_indexes(self, payload):
        f"""
        :payload correlationId: str: previousItem: dict[id: int: sortIndex: int]: item: dict[id: int: sortIndex: int]
        """
        response = requests.put(
            url=self._endpoint.put_feature_group_change_sort_indexes(),
            json=payload,
            headers=self._header.cms_token
        )
        return response
