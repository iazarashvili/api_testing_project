base_url = 'https://reporting.staging.extra.ge/order-reservation'


class OrderReservationReportEndpoints:

    @staticmethod
    def get_order_reservation_items_excel():
        return 'https://reporting.staging.extra.ge/order-reservation/excel'

    @staticmethod
    def get_order_line_reservation_item_excel():
        return 'https://reporting.staging.extra.ge/order-line-reservation-items/excel'
