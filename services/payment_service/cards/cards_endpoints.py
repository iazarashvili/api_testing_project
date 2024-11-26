from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.payment_endpoint}/cards'


class CardsEndpoints:

    @staticmethod
    def get_cards():
        return base_url

    @staticmethod
    def post_cards():
        return base_url

    @staticmethod
    def get_by_card_type():
        return f'{base_url}/get-by-card-type'

    @staticmethod
    def get_id_get_card_type(card_id: int):
        return f'{base_url}/{card_id}/get-card-type'

    @staticmethod
    def post_add_card():
        return f'{base_url}/add-card'

    @staticmethod
    def delete_cards_id(card_id: int):
        return f'{base_url}/{card_id}'

    @staticmethod
    def put_change_basic_card():
        return f'{base_url}/change-basic-card'
