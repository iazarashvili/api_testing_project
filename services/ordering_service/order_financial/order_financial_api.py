import requests
import allure

from services.ordering_service.order_financial.order_financial_endpoints import OrderFinancialEndpoints
from config.headers import Headers


class OrderFinancialApi:
    def __init__(self):
        super().__init__()
        self._endpoints = OrderFinancialEndpoints()
        self._headers = Headers()

    def put_status(self, payload):
        response = requests.put(
            url=self._endpoints.put_status(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_id_dept(self, order_id: str):
        response = requests.get(
            url=self._endpoints.get_id_dept(order_id),
            headers=self._headers.cms_token
        )
        return response

    def get_dept(self):
        response = requests.get(
            url=self._endpoints.get_dept(),
            headers=self._headers.cms_token
        )
        return response

    def get_details(self, params):
        response = requests.get(
            url=self._endpoints.get_dept(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
