import requests
import allure
from services.catalog_service.date.date_endpoints import DateEndpoints
from config.headers import Headers


class DateApi:
    def __init__(self):
        super().__init__()
        self._endpoints = DateEndpoints()
        self._headers = Headers()

    @allure.step('GET data now utc')
    def get_date_now_utc(self):
        response = requests.get(
            url=self._endpoints.get_date_now_utc,
            headers=self._headers.web_token
        )
        return response

    @allure.step('POST data now utc')
    def post_date_now_utc(self):
        response = requests.post(
            url=self._endpoints.post_date_now_utc,
            headers=self._headers.web_token
        )
        return response
