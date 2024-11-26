import requests
import allure

from services.notification_services.profile_notification.profile_notification_endpoints import ProfileNotificationEndpoints
from config.headers import Headers


class ProfileNotificationApi:
    def __init__(self):
        super().__init__()
        self._endpoints = ProfileNotificationEndpoints()
        self._headers = Headers()

    @allure.step('GET profile notification')
    def get_profile_notification(self, params):
        response = requests.get(
            url=self._endpoints.get_profile_notification(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST profile notification')
    def post_profile_notification(self, payload):
        response = requests.post(
            url=self._endpoints.post_profile_notification(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PATH profile notification id status')
    def patch_profile_notification_id_status(self, any_id, payload):
        response = requests.patch(
            url=self._endpoints.patch_profile_notification_id_status(any_id),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
