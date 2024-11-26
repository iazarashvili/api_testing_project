import requests

from utils.helper import Helper
from services.ordering_service.order_reservation.order_reservation_payloads import OrderReservationPayloads
from services.ordering_service.order_reservation.order_reservation_endpoints import OrderReservationEndpoints
from config.headers import Headers
from utils.helpers.base_helpers import HelpFunctions


class OrderReservationApi(Helper):
    def __init__(self):
        super().__init__()
        self.__endpoints = OrderReservationEndpoints()
        self.__payloads = OrderReservationPayloads()
        self.__headers = Headers()

    def put_change_reservation_status(self, order_gui_id: str, order_reservation_item_id: int, reservation_status: int):
        response = requests.put(
            url=self.__endpoints.put_change_reservation_status(),
            json=self.__payloads.put_change_order_reservation_status(order_gui_id, order_reservation_item_id,
                                                                     reservation_status),
            headers=self.__headers.cms_token
        )
        return response

    def put_reservation_order_item_status(self, payload):
        response = requests.put(
            url=self.__endpoints.put_reservation_order_item_status(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_reservation_order_line_status_multiple(self, payload):
        response = requests.put(
            url=self.__endpoints.put_reservation_order_line_status_multiple(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def get_order_reservation(self, params):
        response = requests.get(
            url=self.__endpoints.get_order_reservations(),
            params=params,
            headers=self.__headers.cms_token
        )
        return response

    def post_order_reservation_status_counts(self, payload):
        response = requests.post(
            url=self.__endpoints.post_order_reservation_status_counts(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def get_reservation_order_line_status_change_histories(self, params):
        response = requests.get(
            url=self.__endpoints.get_reservation_order_line_status_change_histories(),
            params=params,
            headers=self.__headers.cms_token
        )
        return response
