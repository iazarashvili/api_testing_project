from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}/model'


class ModelEndpoints:

    @staticmethod
    def get_model():
        return base_url

    @staticmethod
    def post_model():
        return base_url
