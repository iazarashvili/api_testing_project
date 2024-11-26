from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.marketing_endpoint}/landingpages'


class LandingPagesEndpoints:

    @staticmethod
    def get_landing_pages():
        return f'{base_url}'

    @staticmethod
    def post_landing_pages():
        return f'{base_url}'

    @staticmethod
    def put_landing_pages():
        return f'{base_url}'

    @staticmethod
    def delete_landing_pages():
        return f'{base_url}'

    @staticmethod
    def get_landing_pages_id(any_id: int):
        return f'{base_url}/{any_id}'

    @staticmethod
    def get_id_products(any_id: int):
        return f'{base_url}/{any_id}/products'

    @staticmethod
    def get_by_slug_slug(slug: str):
        return f'{base_url}/by-slug/{slug}'

    @staticmethod
    def post_id_products_add(any_id: int):
        return f'{base_url}/{any_id}/products/add'

    @staticmethod
    def post_id_products_remove(product_id: int):
        return f'{base_url}/{product_id}/products/remove'

    @staticmethod
    def post_id_products_import(product_id: int):
        return f'{base_url}/{product_id}/products/import'
