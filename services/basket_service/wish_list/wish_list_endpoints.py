from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.basket_endpoint}wishlist'


class WishListEndpoints:
    @staticmethod
    def post_add_product():
        return f'{base_url}/add-product'

    @staticmethod
    def get_products():
        return f'{base_url}/get-products'

    @staticmethod
    def delete_remove_product(product_id):
        return f'{base_url}/remove-product/{product_id}'

    get_product_ids = f'{base_url}/product-ids'
