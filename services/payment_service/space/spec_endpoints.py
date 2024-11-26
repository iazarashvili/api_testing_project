import uuid

from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.payment_endpoint}/spec'


class SpecEndpoints:

    @staticmethod
    def post_create_qr():
        return f'{base_url}/create-qr?requestId={uuid.uuid4()}'

    @staticmethod
    def get_check_status():
        return f'{base_url}/check-status'

    @staticmethod
    def post_status_update():
        return f'{base_url}/status-update'
