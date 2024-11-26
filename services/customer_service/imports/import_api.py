import allure
import requests

from services.customer_service.imports.import_endpoints import ImportEndpoints
from config.headers import Headers


class ImportApi:

    def __init__(self):
        super().__init__()
        self._endpoints = ImportEndpoints()
        self._headers = Headers()

    @allure.step('POST Import timeslots')
    def post_import_timeslots(self):
        response = requests.post(
            url=self._endpoints.post_import_timeslots(),
            headers=self._headers.cms_token
        )
        return response
