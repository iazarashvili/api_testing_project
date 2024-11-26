from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.customer_endpoint}/juridical'


class JuridicalEndpoints:

    @staticmethod
    def put_juridical():
        return base_url

    @staticmethod
    def get_juridical():
        return base_url

    @staticmethod
    def get_juridical_list():
        return f'{base_url}/list'

    @staticmethod
    def get_contact_phone_exists_phone_number(phone_number):
        return f'{base_url}/contact-phone/exists/{phone_number}'
