from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/reports'


class ReportsEndpoints:

    @staticmethod
    def get_orders():
        return f'{base_url}/orders'

    @staticmethod
    def get_order_items():
        return f'{base_url}/order_items'

    @staticmethod
    def get_shipping_packages():
        return f'{base_url}/shipping-packages'
