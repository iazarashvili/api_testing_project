import allure
import requests
from services.catalog_service.notification.notification_endpoints import NotificationEndpoints


class NotificationApi:

    def __init__(self):
        super().__init__()
        self._endpoints = NotificationEndpoints()

    @allure.step('POST notification send feature add mail')
    def post_send_feature_add_mail(self, payload):
        """
        :param payload: message: str
        """
        response = requests.post(
            url=self._endpoints.post_send_feature_add_mail(),
            json=payload
        )
        return response
