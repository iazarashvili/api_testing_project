from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.reporting_endpoint}/customer'


class CustomerEndpoints:

    @staticmethod
    def get_customer_excel():
        return f'{base_url}/excel'

    @staticmethod
    def get_balance_excel():
        return f'{base_url}/balance/excel'

    @staticmethod
    def get_keywords_excel():
        return f'{base_url}/keywords/excel'
