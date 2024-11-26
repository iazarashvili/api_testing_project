from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}/merchants'


class MerchantsEndpoints:

    @staticmethod
    def get_merchants_user_slug(user_slug):
        return f'{base_url}/{user_slug}'

    @staticmethod
    def get_merchants_slug_details(slug):
        return f'{base_url}/{slug}/details'
