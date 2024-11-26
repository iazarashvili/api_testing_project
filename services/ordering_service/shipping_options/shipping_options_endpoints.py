import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/shippingoptions'


class ShippingOptionsEndpoints:

    @staticmethod
    def post_shipping_options():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_shipping_options():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def get_shipping_options():
        return base_url

    @staticmethod
    def patch_id_status(option_id: int):
        return f'{base_url}/{option_id}/status?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_shipping_options_id(option_id: int):
        return f'{base_url}/{option_id}?requestId={uuid.uuid4()}'

    @staticmethod
    def get_shipping_options_id(option_id: int):
        return f'{base_url}/{option_id}'
