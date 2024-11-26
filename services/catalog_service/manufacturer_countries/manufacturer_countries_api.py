import allure
import requests

from services.catalog_service.manufacturer_countries.manufacturer_countries_endpoints import \
    ManufacturerCountriesEndpoints
from config.headers import Headers


class ManufacturerCountriesApi:

    def __init__(self):
        super().__init__()
        self._endpoints = ManufacturerCountriesEndpoints
        self._headers = Headers

    @allure.step('GET manufacturer countries')
    def get_manufacturer_countries(self, params):
        response = requests.get(
            url=self._endpoints.get_manufacturer_countries(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
