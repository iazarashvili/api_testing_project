import requests
import allure

from services.payment_service.cards.cards_endpoints import CardsEndpoints
from config.headers import Headers


class PaymentCardsApi:
    def __init__(self):
        super().__init__()
        self._endpoints = CardsEndpoints()
        self._headers = Headers()

    @allure.step('GET cards')
    def get_cards(self, params):
        response = requests.get(
            url=self._endpoints.get_cards(),
            headers=self._headers.cms_token,
            params=params
        )
        return response

    @allure.step('POST cards')
    def post_cards(self, params):
        response = requests.post(
            url=self._endpoints.post_cards(),
            headers=self._headers.cms_token,
            params=params
        )
        return response

    @allure.step('GET by card type')
    def get_by_card_type(self, params):
        response = requests.get(
            url=self._endpoints.get_by_card_type(),
            headers=self._headers.cms_token,
            params=params
        )
        return response

    @allure.step('GET id get card type')
    def get_id_get_card_type(self, card_id: int):
        response = requests.get(
            url=self._endpoints.get_id_get_card_type(card_id),
            headers=self._headers.cms_token,
        )
        return response

    @allure.step('POST add card')
    def post_add_card(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_card(),
            headers=self._headers.cms_token,
            json=payload
        )
        return response

    @allure.step('DELETE cards id')
    def delete_cards_id(self, card_id):
        response = requests.delete(
            url=self._endpoints.delete_cards_id(card_id),
            headers=self._headers.cms_token,
        )
        return response

    @allure.step('PUT change basic card')
    def put_change_basic_card(self, payload):
        response = requests.put(
            url=self._endpoints.put_change_basic_card(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response
