from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.payment_endpoint}/installments'


class InstallmentsEndpoints:

    @staticmethod
    def post_installments():
        return base_url

    @staticmethod
    def get_ipay_check_status():
        return f'{base_url}/ipay/check-status'

    @staticmethod
    def get_tbc_check_status():
        return f'{base_url}/tbc/check-status'
