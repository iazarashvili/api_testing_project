import allure
import requests

from services.catalog_service.model.model_endpoint import ModelEndpoints
from services.catalog_service.model.model_payload import ModelPayloads
from config.headers import Headers


class ModelApi:

    def __init__(self):
        super().__init__()
        self._endpoints = ModelEndpoints()
        self._headers = Headers()
        self._payloads = ModelPayloads()

    def get_model(self, params):
        """
        :param params: searchValue: str: pageNumber: int: pageSize: int
        :return:
        """
        response = requests.get(
            url=self._endpoints.get_model(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def post_model(self, payload):
        """
        :param payload:
        :return:
        """
        response = requests.get(
            url=self._endpoints.post_model(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
