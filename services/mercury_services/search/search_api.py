import requests

from utils.helper import Helper
from services.mercury_services.search.search_endpoints import SearchEndpoint
from config.headers import Headers


class SearchApi(Helper):
    def __init__(self):
        super().__init__()
        self._endpoints = SearchEndpoint()
        self._headers = Headers()

    def post_search_go_go(self, payload: str):
        """
        :param payload: searchText: str
        """
        response = requests.post(
            url=self._endpoints.post_search_go_go,
            json=payload,
            headers=self._headers.web_token
        )
        return response

    def post_search_billie_jean(self, payload):
        response = requests.post(
            url=self._endpoints.post_search_billie_jean,
            json=payload,
            headers=self._headers.web_token
        )
        return response

    def post_cool_cat(self, payload):
        response = requests.post(
            url=self._endpoints.post_search_cool_cat,
            json=payload,
            headers=self._headers.web_token
        )
        return response

    def post_mamma_mia(self, payload):
        response = requests.post(
            url=self._endpoints.post_search_cool_cat,
            json=payload,
            headers=self._headers.web_token
        )
        return response

    def post_sunny(self, payload):
        response = requests.post(
            url=self._endpoints.post_sunny,
            json=payload,
            headers=self._headers.web_token
        )
        return response
