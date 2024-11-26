import uuid

from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/locations'


class LocationsEndpoints:

    @staticmethod
    def put_setdefault_delivery_days():
        return f'{base_url}/setdefaultdeliverydays'

    @staticmethod
    def post_locations():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_locations():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_locations():
        return base_url

    @staticmethod
    def get_locations():
        return base_url

    @staticmethod
    def put_delivery_date():
        return f'{base_url}/deliverydate?requestId={uuid.uuid4()}'

    @staticmethod
    def get_locations_id(location_id: str):
        return f'{base_url}/{location_id}'
