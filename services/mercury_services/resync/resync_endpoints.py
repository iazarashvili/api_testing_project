from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.mercury_endpoint}resync'


class ResyncEndpoints:

    @staticmethod
    def get_resync():
        return f'{base_url}'

    @staticmethod
    def get_resync_operation_id(operation_id: str):
        return f'{base_url}{operation_id}'
