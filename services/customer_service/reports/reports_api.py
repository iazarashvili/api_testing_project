import requests

from services.customer_service.reports.reports_endpoints import ReportsEndpoints
from config.headers import Headers


class ReportsApi:

    def __init__(self):
        super().__init__()
        self._endpoints = ReportsEndpoints()
        self._headers = Headers()

    def get_customers(self, params):
        """
        :param params:  From:Date. To: Date
        """
        response = requests.get(
            url=self._endpoints.get_reports_customers(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
