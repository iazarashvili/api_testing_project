import requests
import allure

from services.ordering_service.delivery_order.delivery_order_endpoints import DeliveryOrderEndpoints
from config.headers import Headers


class DeliveryOrderApi:
    def __init__(self):
        super().__init__()
        self._endpoints = DeliveryOrderEndpoints()
        self._headers = Headers()

    @allure.step('PUT delivery order: change delivery order status')
    def put_change_delivery_order_status(self, payload):
        response = requests.put(
            url=self._endpoints.put_change_delivery_order_status(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
