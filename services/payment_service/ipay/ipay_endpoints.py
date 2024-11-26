from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.payment_endpoint}/ipay'


class IpayEndpoints:

    @staticmethod
    def post_payment():
        return f'{base_url}/payment'

    @staticmethod
    def post_reversal():
        return f'{base_url}/reversal'
