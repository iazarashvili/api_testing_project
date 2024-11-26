from utils.data.endpoints_data import Endpoints
import uuid
base_url = f'{Endpoints.catalog_endpoint}features'


class FeaturesEndpoint:

    @staticmethod
    def get_features():
        return f'{base_url}'

    @staticmethod
    def post_features():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_features():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def get_features_id():
        return f'{base_url}'

    @staticmethod
    def put_features_hide():
        return f'{base_url}'

    @staticmethod
    def put_features_change_sort_indexes():
        return f'{base_url}?requestId={uuid.uuid4()}'