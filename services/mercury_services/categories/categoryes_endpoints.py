from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.mercury_endpoint}/categories'


class CategoriesEndpoint:

    @staticmethod
    def get_categories():
        return base_url

    @staticmethod
    def get_categories_identifier(identifier: str):
        return f'{base_url}/{identifier}'

    @staticmethod
    def get_categories_identifier_cheri_cheri(identifier):
        return f'{base_url}/{identifier}/cheri-cheri'
