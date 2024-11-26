import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}/b2c/sync'


class IntegrationEndpoints:

    @staticmethod
    def get_integration_b2c_sync_user_id(user_id):
        return f'{base_url}/{user_id}?requestId={uuid.uuid4()}'
