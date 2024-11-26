import allure
import requests
from services.customer_service.juridical.juridical_endpoints import JuridicalEndpoints
from config.headers import Headers


class JuridicalApi:
    def __init__(self):
        super().__init__()
        self._endpoints = JuridicalEndpoints()
        self._headers = Headers()

    def put_juridical(self, payload):
        """
        :param payload: juridicalTitle: str juridicalId: str
        """
        response = requests.put(
            url=self._endpoints.put_juridical(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_juridical(self, params):
        """
        :param params: JuridicalId: str
        """
        response = requests.get(
            url=self._endpoints.get_juridical(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_juridical_list(self, params):
        """
        :param params: PageSize: int Page: int SearchValue: str
        """
        response = requests.get(
            url=self._endpoints.get_juridical_list(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_contact_phone_exists_phone_number(self, phone_number: str):
        response = requests.get(
            url=self._endpoints.get_contact_phone_exists_phone_number(phone_number),
            headers=self._headers.cms_token
        )
        return response
