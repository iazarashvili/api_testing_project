# import time
#
# import requests
# import json
# import hashlib
#
# import uuid
#
# from utils.izibox_api.izi_box_core_api.courierOrders import CourierOrders
# from utils.izibox_api.izi_box_core_api.customerOrders import CustomerOrders
#
# #  https://delivery-integration-api.staging.extra.ge/swagger/index.html
#
# # def test_first_test(get_izi_box_token):
# #     import hashlib
# #
# #     def create_md5(input_string):
# #         md5 = hashlib.md5()
# #         md5.update(input_string.encode('ascii'))
# #         return md5.hexdigest()
# #
# #     # Example usage:
# #     event_type = 'OrderLineStatusChange'
# #     external_order_line_id = '415580'
# #     status = 'OrderLineDeliveryInProgress'
# #     config_id = '45d6bf81-e8b7-4bfd-8158-508d41ea2f15'
# #
# #     hash_input = f"{event_type}{external_order_line_id}{status}{config_id}"
# #     md5_hash = create_md5(hash_input)
# #     print(md5_hash.upper())
#
#
# # var hash = Extensions.CreateMD5($"{request.EventType}{request.ExternalOrderLineId}{request.Status}{_signinConfig.Id}");
# #
# # public enum EventType
# #     {
# #         OrderStatusChange,
# #         OrderLineStatusChange,
# #         OrderItemStatusChange,
# #         InternalStatusChange
# #     }
#
# # public enum Status
# #    {
# #        OrderLineProcessing = 1,
# #        CourierOrderItemPickedUp = 2,
# #        WarehouseOrderExternalFailed = 3,
# #        WarehouseOrderCanceledExternal = 4,
# #        OrderLinePendingDelivery = 5,
# #        CourierOrderPickedUp = 6,
# #        OrderLineDeliveryInProgress = 7,
# #        OrderLineDelivered = 8,
# #        OrderLineCanceled = 9,
# #        OrderItemProcessing = 10,
# #        OrderItemPendingDelivery = 11,
# #        OrderItemDeliveryInProgress = 12,
# #        OrderItemDelivered = 13,  ეს გვინდა
# #        OrderItemCanceled = 14
# #    }
#
#
# # private DeliveryStatus? TakeDeliveryOrderLineStatus(Status status)
# #        {
# #            switch (status)
# #            {
# #                case Status.OrderLinePendingDelivery:
# #                    return DeliveryStatus.Ready;
# #                case Status.CourierOrderPickedUp:
# #                    return DeliveryStatus.InProgress;
# #                case Status.OrderLineDelivered:
# #                    return DeliveryStatus.Delivered;
# #                default:
# #                    return default;
# #            }
# #        }
# #
# #        private DeliveryOrderLineItemStatus? TakeDeliveryOrderItemStatus(Status status)
# #        {
# #            switch (status)
# #            {
# #                case Status.OrderItemPendingDelivery:
# #                    return DeliveryOrderLineItemStatus.Ready;
# #                case Status.CourierOrderPickedUp:
# #                    return DeliveryOrderLineItemStatus.InProgress;
# #                case Status.OrderItemDelivered:
# #                    return DeliveryOrderLineItemStatus.Delivered;
# #                default:
# #                    return default;
# #            }
# #        }
# #
# # # deliveri inprogresi ერთდროულად დელივერდი
# # 709799, 337163, 709196, 709306, 709389,
# #   709390, 709395, 709396, 709399, 709480, 709490, 617887, 603797,
# #    604759, 608885, 614297, 614616
#
import allure
import pytest

from config.base_api import BaseApi
from utils.helper import Helper
from utils.helpers.base_helpers import HelpFunctions
from services.ordering_service.orders.orders_params import OrderParams


@allure.epic('Basket epic')
class TestFirst(BaseApi, Helper):

    @allure.title('First test')
    @pytest.mark.parametrize('item_count', (2, 2, 4, 4, 4, 4, 4, 4, 4, 4))
    def test_first(self, item_count):
        response = None
        self.basket_api.post_empty_basket()
        response_gimme = self.mercury_products_api.post_gimme([366636, 709402])
        for count in range(len(response_gimme.json()['data'])):
            response = self.basket_api.post_update_basket(response_gimme.json()['data'][count]['id'], response_gimme.json()['data'][count],
                                                          item_count, 23)
        item_json = response.json()['data']
        total_price = response.json()['totalPrice']
        response_checkout = self.ordering_orders_api.post_checkout_prices(item_json, total_price)
        response_order = self.ordering_orders_api.post_orders(response_checkout.json()['data']['products'][0]['items'],
                                                              OrderParams.post_order_params())
        self.payment_api.post_payment_order(response_order.json()['id'])
        reservation_id = self.ordering_orders_api.get_order_lines(response_order.json()['id'])
        for item_id in reservation_id.json()['data'][0]['orderLines']:
            self.ordering_order_reservation_api.put_change_reservation_status(response_order.json()['id'],
                                                                              item_id['orderReservationItemId'], 8)
        hash_list = []
        item_ids = []
        for item_id in reservation_id.json()['data'][0]['orderLines']:
            item_ids.append(item_id['id'])
            hash_list.append(HelpFunctions.create_md5('OrderStatusChange', item_id['id'], 'OrderLineDelivered'))
        for item in range(len(hash_list)):
            self.izi_integration_api.get_webhook(0, 8, item_ids[item], response_order.json()['externalId'],
                                                 hash_list[item])

# # 247991, 679776, 709799, 337163, 709196, 709306, 709389
