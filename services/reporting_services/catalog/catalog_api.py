import requests
import allure

from services.reporting_services.catalog.catalog_endpoints import CatalogEndpoints
from config.headers import Headers


class CatalogReportingApi:

    def __init__(self):
        super().__init__()
        self._endpoints = CatalogEndpoints()
        self._headers = Headers()

    @allure.step('GET catalog full excel')
    def get_full_excel(self, params):
        response = requests.get(
            url=self._endpoints.get_full_excel(),
            headers=self._headers.cms_token,
            params=params
        )
        return response
