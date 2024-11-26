import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/shippingpackages'


class ShippingPackageSizesEndpoints:

    @staticmethod
    def post_shipping_package_sizes():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_shipping_package_sizes():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_shipping_package_sizes():
        return base_url

    @staticmethod
    def get_shipping_package_sizes():
        return base_url

    @staticmethod
    def get_shipping_package_sizes_id(package_size_id: str):
        return f'{base_url}/{package_size_id}'
