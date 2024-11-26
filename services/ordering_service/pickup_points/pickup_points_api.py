import requests
import allure

from services.ordering_service.pickup_points.pickup_points_endpoints import PickupPointsEndpoints
from config.headers import Headers


class PickupPointsApi:
    def __init__(self):
        super().__init__()
        self._endpoints = PickupPointsEndpoints()
        self._headers = Headers()

    def post_pickup_points(self, payload):
        response = requests.post(
            url=self._endpoints.post_pickup_points(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_pickup_points(self, payload):
        response = requests.post(
            url=self._endpoints.put_pickup_points(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def delete_pickup_points(self, params):
        response = requests.delete(
            url=self._endpoints.delete_pickup_points(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_pickup_points(self, params):
        response = requests.get(
            url=self._endpoints.get_pickup_points(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_pickup_points_id(self, any_id):
        response = requests.get(
            url=self._endpoints.get_pickup_points_id(any_id),
            headers=self._headers.cms_token
        )
        return response

    def get_locations(self):
        response = requests.get(
            url=self._endpoints.get_locations(),
            headers=self._headers.cms_token
        )
        return response

    def get_locations_checkout(self, params):
        response = requests.get(
            url=self._endpoints.get_locations_checkout(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
