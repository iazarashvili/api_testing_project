from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}/locations'


class LocationsEndpoints:

    @staticmethod
    def get_locations():
        return f'{base_url}'

    @staticmethod
    def get_locations_id(location_id):
        return f'{base_url}/{location_id}'
