import requests
import allure

from services.ordering_service.reports.reports_endpoints import ReportsEndpoints
from config.headers import Headers


class ReportsApi:
    def __init__(self):
        super().__init__()
        self._endpoints = ReportsEndpoints()
        self._headers = Headers()

    def get_reports_orders(self, params):
        response = requests.get(
            url=self._endpoints.get_orders(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_reports_order_items(self, params):
        response = requests.get(
            url=self._endpoints.get_order_items(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_reports_shipping_packages(self, params):
        response = requests.get(
            url=self._endpoints.get_shipping_packages(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
