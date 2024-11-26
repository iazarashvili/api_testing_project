from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.customer_endpoint}/reports/customers'


class ReportsEndpoints:

    @staticmethod
    def get_reports_customers():
        return base_url
