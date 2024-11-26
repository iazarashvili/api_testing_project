import uuid

from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/orderreservation'


class OrderReservationEndpoints:
    @staticmethod
    def put_change_reservation_status():
        return f'{base_url}/change-reservation-status?requestId={uuid.uuid4()}'

    @staticmethod
    def put_reservation_order_item_status():
        return f'{base_url}/reservation/orderitem/status'

    @staticmethod
    def put_reservation_order_line_status_multiple():
        return f'{base_url}/reservation/orderline/status/multiple'

    @staticmethod
    def get_order_reservations():
        return f'{base_url}/order-reservations'

    @staticmethod
    def post_order_reservation_status_counts():
        return f'{base_url}/order-reservation-status-counts'

    @staticmethod
    def get_reservation_order_line_status_change_histories():
        return f'{base_url}/reservation-order-line-status-histories'
