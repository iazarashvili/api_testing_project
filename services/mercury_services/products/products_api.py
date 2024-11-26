import requests

from services.mercury_services.products.products_endpoints import ProductsEndpoint
from services.mercury_services.products.products_payloads import ProductsPayload
from config.headers import Headers


class ProductsApi:

    def __init__(self):
        super().__init__()
        self._payload = ProductsPayload()
        self._endpoint = ProductsEndpoint()
        self._header = Headers()

    def post_gimme(self, item_ids: list):
        response = requests.post(
            url=self._endpoint.post_gimme,
            json=self._payload.post_gimme_payload(item_ids),
            headers=self._header.web_token
        )
        return response

    def get_products_id(self, product_id):
        response = requests.get(
            url=self._endpoint.get_products_id(product_id),
            headers=self._header.cms_token
        )
        return response
