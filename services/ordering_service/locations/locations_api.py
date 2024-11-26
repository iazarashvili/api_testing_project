import requests
import allure

from services.ordering_service.locations.locations_endpoints import LocationsEndpoints
from config.headers import Headers


class LocationsApi:
    def __init__(self):
        super().__init__()
        self._endpoints = LocationsEndpoints()
        self._headers = Headers()

    def put_set_default_delivery_days(self):
        response = requests.put(
            url=self._endpoints.put_setdefault_delivery_days(),
            headers=self._headers.cms_token
        )
        return response

    def post_locations(self, payload):
        response = requests.post(
            url=self._endpoints.post_locations(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_locations(self, payload):
        response = requests.put(
            url=self._endpoints.put_locations(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def delete_locations(self, params):
        response = requests.delete(
            url=self._endpoints.delete_locations(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_locations(self, params):
        response = requests.get(
            url=self._endpoints.get_locations(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def put_delivery_date(self, payload):
        response = requests.put(
            url=self._endpoints.put_delivery_date(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_locations_id(self, location_id: str, params):
        """
        :param location_id:
        :param params: id: int
        """
        response = requests.get(
            url=self._endpoints.get_locations_id(location_id),
            params=params,
            headers=self._headers.cms_token
        )
        return response
