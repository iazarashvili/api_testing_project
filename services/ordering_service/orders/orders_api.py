import allure
import requests

from services.ordering_service.orders.orders_endpoints import OrdersEndpoints
from services.ordering_service.orders.orders_payloads import OrdersPayload
from services.ordering_service.ordering_models.orders_schema import OrdersSchema
from config.headers import Headers
from utils.helper import Helper


@allure.epic('Orders Api')
class OrdersApi(Helper):
    def __init__(self):
        super().__init__()
        self.__endpoints = OrdersEndpoints()
        self.__payloads = OrdersPayload()
        self.__headers = Headers()

    @allure.step('POST orders')
    def post_orders(self, payloads, params):
        response = requests.post(
            url=self.__endpoints.post_orders(),
            json=self.__payloads.order_payload(payloads),
            params=params,
            headers=self.__headers.web_token
        )
        return response

    def get_orders(self, params):
        response = requests.get(
            url=self.__endpoints.get_orders(),
            params=params,
            headers=self.__headers.cms_token
        )
        return response

    def approve_phone_number(self, payload):
        response = requests.post(
            url=self.__endpoints.post_approve_phone_number(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_update_order(self, payload):
        response = requests.put(
            url=self.__endpoints.put_update_order(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_change_order_cancel_reason(self, payload):
        response = requests.put(
            url=self.__endpoints.put_change_order_cancel_reason(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def post_order_id_product_add(self, order_id, payload):
        response = requests.post(
            url=self.__endpoints.post_order_id_product_add(order_id),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def delete_product_delete_id_order_id(self, product_id, order_id):
        response = requests.delete(
            url=self.__endpoints.delete_product_delete_id_order_id(product_id, order_id),
            headers=self.__headers.cms_token
        )
        return response

    def post_create_order_by_administrator(self, params, payload):
        response = requests.post(
            url=self.__endpoints.post_create_order_by_administrator(),
            params=params,
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_change_order_extra_cash(self, payload):
        response = requests.put(
            url=self.__endpoints.put_change_order_extra_cash(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def order_delivery_type_change(self, payload):
        response = requests.put(
            url=self.__endpoints.put_order_delivery_type_change(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_change_order_bank_of_instalments(self, payload):
        response = requests.put(
            url=self.__endpoints.put_change_order_bank_of_instalments(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_change_merchant_address_for_order(self, payload):
        response = requests.put(
            url=self.__endpoints.put_change_merchant_address_for_order(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_change_order_payment_type(self, payload):
        response = requests.put(
            url=self.__endpoints.put_change_order_payment_type(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_change_order_delivery_method(self, payload):
        response = requests.put(
            url=self.__endpoints.put_change_order_delivery_method(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_change_order_comment(self, payload):
        response = requests.put(
            url=self.__endpoints.put_change_order_comment(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_change_order_line_comment(self, payload):
        response = requests.put(
            url=self.__endpoints.put_change_order_line_comment(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_change_order_general_status(self, payload):
        response = requests.put(
            url=self.__endpoints.put_change_order_general_status(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_order_line_general_status(self, payload):
        response = requests.put(
            url=self.__endpoints.put_order_line_general_status(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_change_merchant_will_pickup(self, payload):
        response = requests.put(
            url=self.__endpoints.put_change_merchant_will_pickup(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def patch_owner_employee(self, payload):
        response = requests.patch(
            url=self.__endpoints.patch_owner_employee(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_order_item_merchant_will_pickup(self, payload):
        response = requests.put(
            url=self.__endpoints.put_order_item_merchant_will_pickup(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def post_order_lines_order_item(self, payload):
        response = requests.post(
            url=self.__endpoints.post_order_lines_order_item(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def delete_order_lines_order_item(self, payload):
        response = requests.delete(
            url=self.__endpoints.delete_order_lines_order_item(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_order_item_general_status(self, payload):
        response = requests.put(
            url=self.__endpoints.put_order_item_general_status(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_merchant_address_order_item(self, payload):
        response = requests.put(
            url=self.__endpoints.put_merchant_address_order_item(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_order_item_comment(self, payload):
        response = requests.put(
            url=self.__endpoints.put_order_item_comment(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_order_general_status_for_admin(self, payload):
        response = requests.put(
            url=self.__endpoints.put_order_general_status_for_admin(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def post_change_order_status_multiple(self, payload):
        response = requests.post(
            url=self.__endpoints.post_change_order_status_multiple(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_order_line_delivery_date(self, payload):
        response = requests.put(
            url=self.__endpoints.put_order_line_delivery_date(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def put_order_line_external_failed_action(self, params):
        response = requests.put(
            url=self.__endpoints.put_order_line_external_failed_action(),
            params=params,
            headers=self.__headers.cms_token
        )
        return response

    def put_order_item_external_failed_action(self, params):
        response = requests.put(
            url=self.__endpoints.put_order_item_external_failed_action(),
            params=params,
            headers=self.__headers.cms_token
        )
        return response

    def post_check_valid_timeslot(self, payload):
        response = requests.post(
            url=self.__endpoints.post_check_valid_timeslot(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def get_orders_id(self, order_id: str):
        response = requests.get(
            url=self.__endpoints.get_orders_id(order_id),
            headers=self.__headers.cms_token
        )
        return response

    def get_orders_id_order_line(self, order_id: str):
        response = requests.get(
            url=self.__endpoints.get_id_order_lines(order_id),
            headers=self.__headers.cms_token
        )
        return response

    def get_id_order_status_change_history(self, order_id: str):
        response = requests.get(
            url=self.__endpoints.get_id_order_status_change_history(order_id),
            headers=self.__headers.cms_token
        )
        return response

    def get_last_order_details(self):
        response = requests.get(
            url=self.__endpoints.get_last_order_details(),
            headers=self.__headers.web_token
        )
        return response

    def get_for_customer_web(self, params):
        response = requests.get(
            url=self.__endpoints.get_for_customer_web(),
            params=params,
            headers=self.__headers.cms_token
        )
        return response

    def get_orders_id_for_customer(self, order_id: str):
        response = requests.get(
            url=self.__endpoints.get_id_for_customer(order_id),
            headers=self.__headers.cms_token
        )
        return response

    def get_orders_id_for_payment(self, order_id: str):
        response = requests.get(
            url=self.__endpoints.get_id_for_payment(order_id),
            headers=self.__headers.cms_token
        )
        return response

    def get_order_line_status_change_history(self, params):
        response = requests.get(
            url=self.__endpoints.get_order_line_status_change_history(),
            params=params,
            headers=self.__headers.cms_token
        )
        return response

    def get_order_products_view(self, params):
        response = requests.get(
            url=self.__endpoints.get_order_products_view(),
            params=params,
            headers=self.__headers.cms_token
        )
        return response

    def post_order_change_histories(self, payload):
        response = requests.post(
            url=self.__endpoints.post_order_change_histories(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    # def post_checkout_prices(self, payload):
    #     response = requests.post(
    #         url=self.__endpoints.post_checkout_prices(),
    #         json=payload,
    #         headers=self.__headers.cms_token
    #     )
    #     return response

    def post_success_page_shipping_info_text(self, payload):
        response = requests.post(
            url=self.__endpoints.post_success_page_shipping_info_text(),
            json=payload,
            headers=self.__headers.cms_token
        )
        return response

    def get_order_invoice(self, params):
        response = requests.get(
            url=self.__endpoints.get_order_invoice(),
            params=params,
            headers=self.__headers.web_token
        )
        return response

    def get_orders_tracking(self):
        response = requests.get(
            url=self.__endpoints.get_tracking(),
            headers=self.__headers.cms_token
        )
        return response

    # ----------------------------------------------------------------------------------

    def get_order_lines(self, order_gui_id):
        response = requests.get(
            url=self.__endpoints.get_order_id_order_lines(order_gui_id),
            headers=self.__headers.cms_token
        )
        return response

    def post_checkout_prices(self, item_json, total_price):
        response = requests.post(
            url=self.__endpoints.post_checkout_prices,
            json=self.__payloads.post_checkout_prices_payload(item_json, total_price),
            headers=self.__headers.web_token
        )
        return response
