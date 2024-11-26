import requests
import allure

from services.catalog_service.features.features_endpoints import FeaturesEndpoint
from config.headers import Headers


class FeaturesApi:

    def __init__(self):
        super().__init__()
        self._headers = Headers()
        self._endpoints = FeaturesEndpoint()

    @allure.step('GET features')
    def get_features(self, params):
        response = requests.get(
            url=self._endpoints.get_features(),
            params=params,
            headers=self._headers.web_token
        )
        return response

    @allure.step('POST features')
    def post_features(self, payload):
        """
        Correlation ID: Optional[str] = None
        Feature Group ID: Optional[int] = None
        Signature: Optional[str] = None
        Status: Optional[int] = None
        Type: Optional[int] = None
        """
        response = requests.post(
            url=self._endpoints.post_features(),
            json=payload,
            headers=self._headers.web_token
        )
        return response

    @allure.step('PUT features')
    def put_features(self, payload):
        """
        Correlation ID: Optional[str] = None
        id: Optional[int] = None
        Feature Group ID: Optional[int] = None
        Signature: Optional[str] = None
        Status: Optional[int] = None
        Type: Optional[int] = None
        """
        response = requests.put(
            url=self._endpoints.put_features(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET features id')
    def get_features_id(self, params):
        response = requests.get(
            url=self._endpoints.get_features_id(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT features hide')
    def put_features_hide(self, payload):
        """
        Correlation ID: Optional[str] = None
        id: Optional[int] = None
        """
        response = requests.put(
            url=self._endpoints.put_features_hide(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT features change sort indexes')
    def put_features_change_sort_indexes(self, payload):
        """
        :payload:
            :correlationId: str
            :previousItem list[id: int: sortIndex: int]
            :item list[id: int: sortIndex: int]
        """
        response = requests.put(
            url=self._endpoints.put_features_change_sort_indexes(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
