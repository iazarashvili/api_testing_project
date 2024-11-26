from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/orderfinancial'


class OrderFinancialEndpoints:

    @staticmethod
    def put_status():
        return f'{base_url}/status'

    @staticmethod
    def get_id_dept(order_id: str):
        return f'{base_url}/{order_id}/dept'

    @staticmethod
    def get_dept():
        return f'{base_url}/dept'

    @staticmethod
    def get_details():
        return f'{base_url}/details'
