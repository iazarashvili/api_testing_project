import requests

from utils.helper import Helper
from services.payment_service.payment.payment_payloads import PaymentPayloads
from services.payment_service.payment.payment_endpoints import PaymentEndpoints
from utils.helpers.base_helpers import HelpFunctions
from config.headers import Headers


class PaymentApi(Helper):
    def __init__(self):
        super().__init__()
        self._endpoints = PaymentEndpoints()
        self.payloads = PaymentPayloads()
        self._headers = Headers()

    def post_balance_refill(self, payload):
        response = requests.post(
            url=self._endpoints.post_balance_refill(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_payment_order(self, order_id):
        response = requests.post(
            url=self._endpoints.post_order(),
            json=self.payloads.post_payment(order_id),
            headers=self._headers.web_token
        )
        return response

    def post_order_reversal(self, payload):
        response = requests.post(
            url=self._endpoints.post_order_reversal(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_order_shipping_service(self, payload):
        response = requests.post(
            url=self._endpoints.post_shipping_service(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_order_premium_service(self, payload):
        response = requests.post(
            url=self._endpoints.post_order_premium_service(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_status(self, params):
        response = requests.get(
            url=self._endpoints.get_status(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_status_order(self, params):
        response = requests.get(
            url=self._endpoints.get_status_order(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_redirect_status_transaction_id(self, status, transaction_ir):
        response = requests.get(
            url=self._endpoints.get_redirect_status_transaction_id(status, transaction_ir),
            headers=self._headers.cms_token
        )
        return response

    def post_sponsorship(self, payload):
        """
        :param payload: id: int
        """
        response = requests.post(
            url=self._endpoints.post_sponsorship(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_order_dept(self, payload):
        response = requests.post(
            url=self._endpoints.post_order_dept(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
