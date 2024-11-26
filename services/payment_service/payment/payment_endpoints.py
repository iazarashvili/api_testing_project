import uuid

from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.payment_endpoint}'


class PaymentEndpoints:

    @staticmethod
    def post_balance_refill():
        return f'{base_url}/balance-refill?requestId={uuid.uuid4()}'

    @staticmethod
    def post_order():
        return f'{base_url}/order?requestId={uuid.uuid4()}'

    @staticmethod
    def post_order_reversal():
        return f'{base_url}/order/reversal?requestId={uuid.uuid4()}'

    @staticmethod
    def post_shipping_service():
        return f'{base_url}/order/shipping-service?requestId={uuid.uuid4()}'

    @staticmethod
    def post_order_premium_service():
        return f'{base_url}/order/premium-service?requestId={uuid.uuid4()}'

    @staticmethod
    def get_status():
        return f'{base_url}/status'

    @staticmethod
    def get_status_order():
        return f'{base_url}status/order'

    @staticmethod
    def get_redirect_status_transaction_id(status, transaction_id):
        return f'{base_url}/redirect/{status}/{transaction_id}'

    @staticmethod
    def post_sponsorship():
        return f'{base_url}/sponsorship?requestId={uuid.uuid4()}'

    @staticmethod
    def post_order_dept():
        return f'{base_url}/order/dept'

    # post_balance_refill = f'{base_url}balance-refill?requestId={uuid.uuid4()}'
