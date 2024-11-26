import requests
import allure

from services.ordering_service.promo_codes.promo_codes_endpoints import PromoCodesEndpoints
from config.headers import Headers


class PromoCodesApi:
    def __init__(self):
        super().__init__()
        self._endpoints = PromoCodesEndpoints()
        self._headers = Headers()

    def post_generate_promo_code(self, payload):
        response = requests.post(
            url=self._endpoints.post_generate_promo_code(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_update_promo_code(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_promo_code(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_change_promo_code_status(self, payload):
        response = requests.put(
            url=self._endpoints.put_change_promo_code_status(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_add_multiple_promo_code(self, params):
        response = requests.post(
            url=self._endpoints.post_add_multiple_promo_code(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def post_promo_codes_id_products(self, promo_id: int, payload):
        response = requests.post(
            url=self._endpoints.post_id_products(promo_id),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def delete_id_products(self, promo_id: int, payload: list):
        response = requests.delete(
            url=self._endpoints.delete_id_products(promo_id),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def delete_id_products_clear(self, promo_id: int):
        response = requests.delete(
            url=self._endpoints.delete_id_products_clear(promo_id),
            headers=self._headers.cms_token
        )
        return response

    def get_promo_code_details_promo_code_id(self, promo_code_id: int):
        response = requests.get(
            url=self._endpoints.get_promo_code_details_promo_code_id(promo_code_id),
            headers=self._headers.cms_token
        )
        return response

    def get_promo_code_validation_promo_code(self, promo_code: str, params):
        response = requests.get(
            url=self._endpoints.get_promo_code_validation_promo_code(promo_code),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_promo_codes(self, params):
        response = requests.get(
            url=self._endpoints.get_promo_codes(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_id_products(self, params, promo_code_id):
        response = requests.get(
            url=self._endpoints.get_id_products(promo_code_id),
            params=params,
            headers=self._headers.cms_token
        )
        return response
