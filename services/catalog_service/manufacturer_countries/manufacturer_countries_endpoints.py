from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}/manufacturercountries'


class ManufacturerCountriesEndpoints:

    @staticmethod
    def get_manufacturer_countries():
        return base_url
