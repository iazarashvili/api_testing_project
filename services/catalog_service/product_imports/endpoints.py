import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}/productimports'


class ProductImportsEndpoint:

    @staticmethod
    def post_import_multiple():
        return f'{base_url}/import-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_stock_and_prices_update_multiple():
        return f'{base_url}/product-stock-and-prices-update-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_assets_import_multiple():
        return f'{base_url}/product-assets-import-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def product_details_update_multiple():
        return f'{base_url}/product-details-update-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_categories_update_multiple():
        return f'{base_url}/product-categories-update-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_shipping_package_size_update_multiple():
        return f'{base_url}/product-shipping-package-sizes-update-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_keywords_update_multiple():
        return f'{base_url}/product-keywords-update-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def post_import_variations():
        return f'{base_url}/importvariations?requestId={uuid.uuid4()}'

    @staticmethod
    def post_import_delete_products():
        return f'{base_url}/importdeleteproducts?requestId={uuid.uuid4()}'

    @staticmethod
    def product_brands_and_models_update_multiple():
        return f'{base_url}/product-brands-and-models-update-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_has_best_price_change_multiple():
        return f'{base_url}/product-has-best-price-change-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_update_has_gift_multiple():
        return f'{base_url}/product-update-hasgift-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_add_bundles():
        return f'{base_url}/product-add-bundles?requestId={uuid.uuid4()}'

    @staticmethod
    def post_rs_product_title():
        return f'{base_url}/rs-product-title?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_expiration_date():
        return f'{base_url}/product-expiration-date?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_sort_index():
        return f'{base_url}/product-sort-index?requestId={uuid.uuid4()}'

    @staticmethod
    def post_product_merchant():
        return f'{base_url}/product-mercant?requestId={uuid.uuid4()}'
