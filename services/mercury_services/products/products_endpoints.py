from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.mercury_endpoint}/products'


class ProductsEndpoint:
    post_gimme = f'{base_url}/gimme'

    @staticmethod
    def get_products_id(product_id):
        return f'{base_url}/{product_id}'
