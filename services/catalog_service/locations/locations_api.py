import allure
import requests

from services.catalog_service.locations.locations_endpoints import LocationsEndpoints
from config.headers import Headers


class LocationApi:

    def __init__(self):
        super().__init__()
        self._endpoints = LocationsEndpoints()
        self._headers = Headers

    @allure.step('GET locations')
    def get_locations(self, params):
        response = requests.get(
            url=self._endpoints.get_locations(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET locations id')
    def get_locations_id(self, location_id: int):
        response = requests.get(
            url=self._endpoints.get_locations_id(location_id),
            headers=self._headers.cms_token
        )
        return response
