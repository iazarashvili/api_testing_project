import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/vouchers'


class VouchersEndpoints:

    @staticmethod
    def post_vouchers():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def get_validate():
        return f'{base_url}/validate'

    @staticmethod
    def get_details():
        return f'{base_url}/details'
