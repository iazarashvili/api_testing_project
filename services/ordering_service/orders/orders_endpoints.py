import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/orders'


class OrdersEndpoints:

    @staticmethod
    def post_orders():
        return f'{base_url}'

    @staticmethod
    def get_orders():
        return base_url

    @staticmethod
    def post_approve_phone_number():
        return f'{base_url}/approve_phone_number?requestId={uuid.uuid4()}'

    @staticmethod
    def put_update_order():
        return f'{base_url}/update-order?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_order_cancel_reason():
        return f'{base_url}/change-order-cancel-reason?requestId={uuid.uuid4()}'

    @staticmethod
    def post_order_id_product_add(order_id):
        return f'{base_url}/{order_id}/product/add?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_product_delete_id_order_id(product_id, order_id):
        return f'{base_url}/product/{product_id}/{order_id}?requestId={uuid.uuid4()}'

    @staticmethod
    def post_create_order_by_administrator():
        return f'{base_url}/createorderbyadministrator'

    @staticmethod
    def put_change_order_extra_cash():
        return f'{base_url}/change-order-extracash?requestId={uuid.uuid4()}'

    @staticmethod
    def put_order_delivery_type_change():
        return f'{base_url}/order-deliverytype-change?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_order_bank_of_instalments():
        return f'{base_url}/change_order_bank_of_instalments?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_merchant_address_for_order():
        return f'{base_url}/change-merchantaddress-for-order?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_order_payment_type():
        return f'{base_url}/change-order-paymenttype?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_order_delivery_method():
        return f'{base_url}change-order-deliverymethod?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_order_comment():
        return f'{base_url}/change-order-comment?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_order_line_comment():
        return f'{base_url}change-orderline-comment?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_order_general_status():
        return f'{base_url}/change-order-general-status?requestId={uuid.uuid4()}'

    @staticmethod
    def put_order_line_general_status():
        return f'{base_url}/orderline/general/status?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_merchant_will_pickup():
        return f'{base_url}/change-merchant-will-pickup?requestId={uuid.uuid4()}'

    @staticmethod
    def patch_owner_employee():
        return f'{base_url}/owner-employee?requestId={uuid.uuid4()}'

    @staticmethod
    def put_order_item_merchant_will_pickup():
        return f'{base_url}/orderitem/merchant/will/pickup?requestId={uuid.uuid4()}'

    @staticmethod
    def post_order_lines_order_item():
        return f'{base_url}/orderlines/orderitem?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_order_lines_order_item():
        return f'{base_url}/orderlines/orderitem?requestId={uuid.uuid4()}'

    @staticmethod
    def put_order_item_general_status():
        return f'{base_url}/orderitem/general/status?requestId={uuid.uuid4()}'

    @staticmethod
    def put_merchant_address_order_item():
        return f'{base_url}/merchant/address/orderitem?requestId={uuid.uuid4()}'

    @staticmethod
    def put_order_item_comment():
        return f'{base_url}/orderitem/comment?requestId={uuid.uuid4()}'

    @staticmethod
    def put_order_general_status_for_admin():
        return f'{base_url}/order/general/status/for/admin?requestId={uuid.uuid4()}'

    @staticmethod
    def post_change_order_status_multiple():
        return f'{base_url}/change-order-status-multiple?requestId={uuid.uuid4()}'

    @staticmethod
    def put_order_line_delivery_date():
        return f'{base_url}/orderline/deliverydate?requestId={uuid.uuid4()}'

    @staticmethod
    def put_order_line_external_failed_action():
        return f'{base_url}/orderline/externalfailedaction'

    @staticmethod
    def put_order_item_external_failed_action():
        return f'{base_url}/orderitem/externalfailedaction'

    @staticmethod
    def post_check_valid_timeslot():
        return f'{base_url}/check/valid-timeslot?requestId={uuid.uuid4()}'

    @staticmethod
    def get_orders_id(order_id: str):
        return f'{base_url}/{order_id}'

    @staticmethod
    def get_id_order_lines(order_line_id: str):
        return f'{base_url}/{order_line_id}/order-lines'

    @staticmethod
    def get_id_order_status_change_history(order_id: str):
        return f'{base_url}/{order_id}/order-status-change-history'

    @staticmethod
    def get_last_order_details():
        return f'{base_url}/last-order-details'

    @staticmethod
    def get_for_customer_web():
        return f'{base_url}/for-customer-web'

    @staticmethod
    def get_id_for_customer(order_id: str):
        return f'{base_url}/{order_id}/for-customer'

    @staticmethod
    def get_id_for_payment(order_id: str):
        return f'{base_url}/{order_id}/for-payment'

    @staticmethod
    def get_order_line_status_change_history():
        return f'{base_url}/getorderlinestatuschangehistory'

    @staticmethod
    def get_order_products_view():
        return f'{base_url}/getorderproductview'

    @staticmethod
    def post_order_change_histories():
        return f'{base_url}/order-change-histories'

    @staticmethod
    def get_checkout_prices():
        return f'{base_url}/checkout-prices'

    @staticmethod
    def post_success_page_shipping_info_text():
        return f'{base_url}/success-page-shipping-info-text'

    @staticmethod
    def get_order_invoice():
        return f'{base_url}/order-invoice'

    @staticmethod
    def get_tracking():
        return f'{base_url}/tracking'

    # post_orders = lambda self, user_type: f'{base_url}?requestId={uuid.uuid4()}&userType={user_type}'

    get_order_id_order_lines = lambda self, order_gui_id: f'{base_url}/{order_gui_id}/order-lines?requestId={uuid.uuid4()}'
    post_checkout_prices = f'{base_url}/checkout-prices?requestId{uuid.uuid4()}'
