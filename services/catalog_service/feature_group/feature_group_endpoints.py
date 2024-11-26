from utils.data.endpoints_data import Endpoints
import uuid

base_url = f'{Endpoints.catalog_endpoint}featuregroup'


class FeatureGroupEndpoint:

    @staticmethod
    def get_feature_group():
        return f'{base_url}'

    @staticmethod
    def post_feature_group():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_feature_group():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_feature_group():
        return f'{base_url}'

    @staticmethod
    def get_feature_group_id():
        return f'{base_url}'

    @staticmethod
    def put_feature_group_change_sort_indexes():
        return f'{base_url}?requestId={uuid.uuid4()}'
