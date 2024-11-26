from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.reporting_endpoint}/catalog'


class CatalogEndpoints:

    @staticmethod
    def get_full_excel():
        return f'{base_url}/full/excel'

    @staticmethod
    def get_stock_and_prices_excel():
        return f'{base_url}/stock-and-prices/excel'

    @staticmethod
    def get_assets_excel():
        return f'{base_url}/assets/excel'

    @staticmethod
    def get_details_excel():
        return f'{base_url}/details/excel'

    @staticmethod
    def get_categories_excel():
        return f'{base_url}/categories/excel'

    @staticmethod
    def get_merchants_excel():
        return f'{base_url}/merchants/excel'

    @staticmethod
    def get_keywords_excel():
        return f'{base_url}/keywords/excel'

    @staticmethod
    def get_guarantees_excel():
        return f'{base_url}/guarantees/excel'

    @staticmethod
    def get_groups_excel():
        return f'{base_url}/groups/excel'

    @staticmethod
    def get_brands_and_models_excel():
        return f'{base_url}/brands-and-models/excel'

    @staticmethod
    def get_product_has_bets_price_guarantee_excel():
        return f'{base_url}/product-has-bets-price-guarantee/excel'

    @staticmethod
    def get_product_has_gift_excel():
        return f'{base_url}/product-has-gift/excel'

    @staticmethod
    def get_content_report_excel():
        return f'{base_url}/content-report/excel'

    @staticmethod
    def get_product_bundles_excel():
        return f'{base_url}/product-bundles/excel'

    @staticmethod
    def get_product_rs_title_excel():
        return f'{base_url}/product-rs-title/excel'

    @staticmethod
    def get_product_expiration_date_excel():
        return f'{base_url}/product-expiration-date/excel'

    @staticmethod
    def get_first_party_products_excel():
        return f'{base_url}/first-party-products/excel'

    @staticmethod
    def get_sponsored_products_report_excel():
        return f'{base_url}/sponsored-products-report/excel'

    @staticmethod
    def get_sort_index_report_excel():
        return f'{base_url}/sort-index-report/excel'

    @staticmethod
    def get_category_tree_excel():
        return f'{base_url}/category-tree/excel'
