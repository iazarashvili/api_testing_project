import requests
import allure

from services.marketing_service.popups.popups_endpoints import PopupsEndpoints
from config.headers import Headers


class PopupsApi:
    def __init__(self):
        super().__init__()
        self._endpoints = PopupsEndpoints()
        self._headers = Headers()

    def post_popups(self, payload):
        response = requests.post(
            url=self._endpoints.post_popups(),
            headers=self._headers.cms_token,
            json=payload
        )
        return response

    def get_popups(self, params: int):
        """
        :param params: type: int: 1, 2, 3
        """
        response = requests.get(
            url=self._endpoints.get_popups(),
            headers=self._headers.cms_token,
            params=params
        )
        return response

    def delete_popups_id(self, popup_id: int):
        response = requests.get(
            url=self._endpoints.delete_popups_id(popup_id),
            headers=self._headers.cms_token
        )
        return response

    def put_popups_id(self, popup_id: int, payload):
        response = requests.get(
            url=self._endpoints.put_popups_id(popup_id),
            headers=self._headers.cms_token,
            json=payload
        )
        return response

    def get_popups_admin_panel(self, payload):
        response = requests.get(
            url=self._endpoints.get_admin_panel(),
            headers=self._headers.cms_token,
            json=payload
        )
        return response

    def post_popups_upload_image(self, payload):
        response = requests.post(
            url=self._endpoints.post_upload_image(),
            headers=self._headers.cms_token,
            json=payload
        )
        return response

    def post_popups_send_email(self, payload):
        response = requests.post(
            url=self._endpoints.post_send_email(),
            headers=self._headers.cms_token,
            json=payload
        )
        return response
