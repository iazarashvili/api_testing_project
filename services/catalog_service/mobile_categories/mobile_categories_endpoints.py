from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}/mobilecategories'


class MobileCategoriesEndpoints:

    @staticmethod
    def get_home_screen_categories():
        return f'{base_url}/home-screen-categories'

    @staticmethod
    def get_home_screen_sub_categories():
        return f'{base_url}/home-screen-sub-categories'

    @staticmethod
    def get_home_screen_special_offers():
        return f'{base_url}/home-screen-special-offers'
