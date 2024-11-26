import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}collectorhub'


class CollectorHubEndpoints:

    @staticmethod
    def post_import_products():
        return f'{base_url}/import-products?requestId={uuid.uuid4()}'

    @staticmethod
    def post_import_product_assets():
        return f'{base_url}/import-product-assets?requestId={uuid.uuid4()}'

    @staticmethod
    def post_update_product_stock_and_price():
        return f'{base_url}/update-product-stock-and-prices?requestId={uuid.uuid4()}'

    @staticmethod
    def post_remove_expired_products():
        return f'{base_url}/remove-expired-products?requestId={uuid.uuid4()}'