import json
import uuid

import requests

url = None
class CourierOrders:

    @staticmethod
    def post_courier_orders_warehouse_order_item_ids(izi_box_token, order_item_ids: list[str], provider_branch_id,
                                                     warehouse_id):
        base_url = f'{url}/api/v1/courierorders/warehouseorders/orderitemids?showSpinner=true'

        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'authorization': 'Bearer ' + izi_box_token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://dashboard.staging.izibox.ge',
            'pragma': 'no-cache',
            'referer': 'https://dashboard.staging.izibox.ge/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-requestid': str(uuid.uuid4())
        }
        payload = json.dumps({
            "orderItemIds": order_item_ids,
            "courierId": "1d686bed-4f15-49e2-8bf1-4b44213e742f",
            "providerBranchId": provider_branch_id,
            "warehouseId": warehouse_id
        })
        response = requests.request("POST", base_url, headers=headers, data=payload)
        return response

    @staticmethod
    def post_courier_orders_accept(courier_token, courier_order_id: str):
        base_url = f'{url}/api/v1/courierorders/accept?showSpinner=true'
        payload = json.dumps({
            "courierOrderId": courier_order_id
        })

        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer ' + courier_token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://dashboard.staging.izibox.ge',
            'pragma': 'no-cache',
            'referer': 'https://dashboard.staging.izibox.ge/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-requestid': str(uuid.uuid4())
        }
        response = requests.request("POST", base_url, headers=headers, data=payload)
        return response

    @staticmethod
    def post_courier_orders_arrive_at_pickup_address(courier_token, courier_order_id: str):
        base_url = f'{url}/api/v1/courierorders/arriveatpickupaddress?showSpinner=true'
        payload = json.dumps({
            "courierOrderId": courier_order_id
        })
        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer ' + courier_token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://dashboard.staging.izibox.ge',
            'pragma': 'no-cache',
            'referer': 'https://dashboard.staging.izibox.ge/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-requestid': str(uuid.uuid4())
        }

        response = requests.request("POST", base_url, headers=headers, data=payload)
        return response

    @staticmethod
    def post_courier_orders_order_items_pickup(courier_token, courier_order_id: str, order_item_ids: list[str]):
        base_url = f'{url}/api/v1/courierorders/orderitems/pickup?showSpinner=true'
        payload = json.dumps({
            "id": courier_order_id,
            "itemIds": order_item_ids
        })
        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer ' + courier_token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://dashboard.staging.izibox.ge',
            'pragma': 'no-cache',
            'referer': 'https://dashboard.staging.izibox.ge/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-requestid': str(uuid.uuid4())
        }

        response = requests.request("POST", base_url, headers=headers, data=payload)
        return response

    @staticmethod
    def post_courier_orders_deliver(courier_token, courier_order_id: list[str]):
        base_url = f'{url}/api/v1/courierorders/deliver?showSpinner=true'
        payload = json.dumps({
            "courierOrderIds": courier_order_id
        })
        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer ' + courier_token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://dashboard.staging.izibox.ge',
            'pragma': 'no-cache',
            'referer': 'https://dashboard.staging.izibox.ge/',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-requestid': str(uuid.uuid4())
        }

        response = requests.request("PUT", base_url, headers=headers, data=payload)
        return response

    @staticmethod
    def post_courier_orders_assign_customer_courier(izi_box_token, order_items_ids: list[str], courier_id):
        base_url = f'{url}/api/v1/courierorders/assign/customer/courier?showSpinner=true'

        payload = json.dumps([
            {
                "orderItemIds": order_items_ids,
                "courierId": courier_id
            }
        ])
        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'authorization': 'Bearer ' + izi_box_token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://dashboard.staging.izibox.ge',
            'pragma': 'no-cache',
            'referer': 'https://dashboard.staging.izibox.ge/',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-requestid': str(uuid.uuid4())
        }

        response = requests.request("POST", base_url, headers=headers, data=payload)
        return response

    @staticmethod
    def get_courier_orders_collected(izi_box_token, external_id):
        base_url = f'{url}/api/v1/courierorders/collected?page=0&pageSize=25&orderId={external_id}&showSpinner=true'

        payload = {}
        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'authorization': 'Bearer ' + izi_box_token,
            'cache-control': 'no-cache',
            'dnt': '1',
            'origin': 'https://dashboard.staging.izibox.ge',
            'pragma': 'no-cache',
            'referer': 'https://dashboard.staging.izibox.ge/',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-requestid': str(uuid.uuid4())
        }

        response = requests.request("GET", base_url, headers=headers, data=payload)
        return response

    @staticmethod
    def post_courier_orders_collected(izi_box_token, courier_order_id):
        base_url = f'{url}/api/v1/courierorders/collected?showSpinner=true'

        payload = json.dumps([{"courierOrderId": courier_order_id}])
        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'authorization': 'Bearer ' + izi_box_token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://dashboard.staging.izibox.ge',
            'pragma': 'no-cache',
            'referer': 'https://dashboard.staging.izibox.ge/',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-requestid': str(uuid.uuid4())
        }

        response = requests.request("POST", base_url, headers=headers, data=payload)
        return response

    @staticmethod
    def put_courier_orders_pick_up(courier_token, courier_order_id):
        base_url = f'{url}/api/v1/courierorders/pickup?showSpinner=true'

        payload = json.dumps({
            "courierOrderId": courier_order_id
        })
        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'authorization': 'Bearer ' + courier_token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://dashboard.staging.izibox.ge',
            'pragma': 'no-cache',
            'referer': 'https://dashboard.staging.izibox.ge/',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-requestid': str(uuid.uuid4())
        }

        response = requests.request("PUT", base_url, headers=headers, data=payload)
        return response
