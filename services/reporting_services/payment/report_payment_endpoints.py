from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.reporting_endpoint}/payment'


class PaymentReportEndpoints:

    @staticmethod
    def get_transaction_details_excel():
        return f'{base_url}/transaction-details/excel'

    @staticmethod
    def get_order_payment_details_excel():
        return f'{base_url}/order/payment/details/excel'

    @staticmethod
    def get_payment_details_excel():
        return f'{base_url}/payment/details/excel'
