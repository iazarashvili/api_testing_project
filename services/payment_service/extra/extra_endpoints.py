from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.payment_endpoint}/extra'


class ExtraEndpoints:

    @staticmethod
    def post_add_balance_from_extra():
        return f'{base_url}/add-balance-from-extra'

    @staticmethod
    def post_remove_balance_from_extra():
        return f'{base_url}/remove-balance-from-extra'

    @staticmethod
    def get_balance_transactions():
        return f'{base_url}/balance-transactions'

    @staticmethod
    def get_order_payment_details():
        return f'{base_url}/order-payment-details'

    @staticmethod
    def post_use_voucher():
        return f'{base_url}/use-voucher'

    @staticmethod
    def get_order_refund_details():
        return f'{base_url}/order-refund-details'
