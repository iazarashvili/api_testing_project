import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/pickuppoints'


class PickupPointsEndpoints:

    @staticmethod
    def post_pickup_points():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_pickup_points():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_pickup_points():
        return base_url

    @staticmethod
    def get_pickup_points():
        return base_url

    @staticmethod
    def get_pickup_points_id(any_id: int):
        return f'{base_url}/{any_id}'

    @staticmethod
    def get_locations():
        return f'{base_url}/locations'

    @staticmethod
    def get_locations_checkout():
        return f'{base_url}/locations/checkout'
