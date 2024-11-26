import requests

from services.delivery_integration_service.izi_box_integration.izi_box_integration_endpoints import \
    IziBoxIntegrationEndpoints
from config.headers import Headers


class IziBoxIntegrationApi:

    def __init__(self):
        super().__init__()
        self.__endpoints = IziBoxIntegrationEndpoints()
        self.__headers = Headers()

    def get_webhook(self, event_type, status, order_line_id, order_id, my_hash):
        response = requests.get(
            url=self.__endpoints.get_webhook(event_type, status, order_line_id, order_id, my_hash),
        )
        return response
