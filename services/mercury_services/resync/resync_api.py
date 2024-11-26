import requests
import allure

from services.mercury_services.resync.resync_endpoints import ResyncEndpoints
from config.headers import Headers


class ResyncApi:
    def __init__(self):
        super().__init__()
        self._endpoints = ResyncEndpoints()
        self._headers = Headers()

    @allure.step('GET resync')
    def get_resync(self):
        response = requests.get(
            url=self._endpoints.get_resync(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET resync operation id')
    def get_resync_operation_id(self, operation_id: str):
        response = requests.get(
            url=self._endpoints.get_resync_operation_id(operation_id),
            headers=self._headers.cms_token
        )
        return response
