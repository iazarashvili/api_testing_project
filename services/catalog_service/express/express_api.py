import allure
import requests

from services.catalog_service.express.express_payloads import ExpressPayloads
from services.catalog_service.express.express_endpoints import ExpressEndpoints
from config.headers import Headers


class ExpressApi:
    def __init__(self):
        super().__init__()
        self._payloads = ExpressPayloads()
        self._endpoints = ExpressEndpoints()
        self._headers = Headers()

    @allure.step('POST express')
    def post_express(self, payload):
        response = requests.post(
            url=self._endpoints.post_express,
            data=self._payloads.post_express(payload),
            headers=self._headers.web_token
        )
        return response

    @allure.step('GET express dark store')
    def get_express_dark_store(self, params):
        response = requests.get(
            url=self._endpoints.get_express_darkstore(),
            params=params,
            headers=self._headers.web_token
        )
        return response
