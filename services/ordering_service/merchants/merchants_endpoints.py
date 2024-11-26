import uuid

from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/merchants'


class MerchantsEndpoints:

    @staticmethod
    def post_sales():
        return f'{base_url}/sales?requestId={uuid.uuid4()}'

    @staticmethod
    def post_sales_averages():
        return f'{base_url}/sales/averages'

    @staticmethod
    def post_sales_top_products():
        return f'{base_url}/sales/top-products'

    @staticmethod
    def post_sales_locations():
        return f'{base_url}/sales/locations'

    @staticmethod
    def post_sales_out_of_stock():
        return f'{base_url}sales/outofstock'

    @staticmethod
    def post_sales_category_ranking():
        return f'{base_url}/sales/category/ranking'

    @staticmethod
    def get_has_active_order():
        return f'{base_url}/has-active-order'
