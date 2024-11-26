import requests
import allure

from services.ordering_service.express_delivery_type.express_delivery_type_endpoints import ExpressDeliveryTypeEndpoints
from config.headers import Headers


class ExpressDeliveryTypeApi:
    def __init__(self):
        super().__init__()
        self._endpoints = ExpressDeliveryTypeEndpoints()
        self._headers = Headers()

    @allure.step('POST express delivery type')
    def post_express_delivery_type(self, payload):
        response = requests.post(
            url=self._endpoints.post_express_delivery_type(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET express delivery type')
    def get_express_delivery_type(self, params):
        response = requests.get(
            url=self._endpoints.get_express_delivery_type(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
