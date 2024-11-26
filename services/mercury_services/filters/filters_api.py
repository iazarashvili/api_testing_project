import requests

from services.mercury_services.filters.filters_endpoints import FiltersEndpoint
from config.headers import Headers


class FiltersApi:

    def __init__(self):
        super().__init__()
        self._endpoints = FiltersEndpoint()
        self._headers = Headers

    def post_beat_it(self, payload):
        response = requests.post(
            url=self._endpoints.post_beat_it(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
