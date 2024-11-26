from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.reporting_endpoint}/basket'


class BasketEndpoints:

    @staticmethod
    def get_abandoned_carts_excel():
        return f'{base_url}/abandoned-cart/excel'

    @staticmethod
    def get_wishlist_products_excel():
        return f'{base_url}/wishlist-products/excel'
