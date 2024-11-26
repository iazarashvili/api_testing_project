import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/shippingpackagesizes'


class ShippingPackagesEndpoints:

    @staticmethod
    def post_shipping_packages():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_shipping_packages():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_shipping_packages():
        return base_url

    @staticmethod
    def get_shipping_packages():
        return base_url

    @staticmethod
    def post_import_multiple():
        return f'{base_url}/import-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_activation():
        return f'{base_url}/change-activation?requestId={uuid.uuid4()}'

    @staticmethod
    def get_shipping_package_id(package_id: int):
        return f'{base_url}{package_id}'

    @staticmethod
    def get_import_template():
        return
