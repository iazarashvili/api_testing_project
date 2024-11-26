from utils.data.endpoints_data import Endpoints
import uuid

base_url = f'{Endpoints.catalog_endpoint}featuresuggestedvalues'


class FeatureSuggestedValuesEndpoints:

    @staticmethod
    def get_feature_suggested_values_category_id_feature_id(category_id, feature_id):
        return f'{base_url}/{category_id}/features/{feature_id}'

    @staticmethod
    def get_feature_suggested_values_id(feature_value_id: int):
        return f'{base_url}/{feature_value_id}'

    @staticmethod
    def post_feature_suggested_values():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_feature_suggested_values():
        return f'{base_url}'

    @staticmethod
    def put_feature_suggested_values_change_status():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_feature_suggested_values_change_sort_index():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_feature_suggested_values_change_feature_suggested_value():
        return f'{base_url}?requestId={uuid.uuid4()}'
