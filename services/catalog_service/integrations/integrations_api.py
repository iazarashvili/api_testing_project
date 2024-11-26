import allure
import requests

from services.catalog_service.integrations.integrations_endpoints import IntegrationEndpoints
from config.headers import Headers


class IntegrationApi:

    def __init__(self):
        super().__init__()
        self._endpoints = IntegrationEndpoints()
        self._headers = Headers()

    @allure.step('GET integration b2c sync user id')
    def get_integrations_b2c_sync_user_id(self, user_id: str):
        response = requests.get(
            url=self._endpoints.get_integration_b2c_sync_user_id(user_id),
            headers=self._headers.cms_token
        )
        return response
