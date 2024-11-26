import json
import uuid

import requests


url = None


class WarehouseOrders:

    @staticmethod
    def get_warehouse_orders_order_id(izi_box_token, order_id):
        base_url = f'{url}/api/v1/warehouseorders/orders/{order_id}?showSpinner=false'
        headers = {
            'authorization': 'Bearer ' + izi_box_token
        }

    # ორდერის მოძებნა საწყობის დეშბორდში
    @staticmethod
    def get_warehouse_orders_arrived_and_not_arrived(izi_box_token, external_id):
        base_url = f'{url}/api/v1/warehouseorders/arrivedandnotarrived?page=0&pageSize=25&id={external_id}&isSortOrder=false&status=4&status=5&showSpinner=true'
        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
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


    @staticmethod
    def put_warehouse_orders_verify(izi_box_token, order_item_ids: list[str]):
        base_url = f'{url}/api/v1/warehouseorders/verify?showSpinner=true'

        payload = json.dumps({
            "orderItemIds": order_item_ids
        })
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

        response = requests.request("PUT", base_url, headers=headers, data=payload)
        return response

    @staticmethod
    def put_warehouse_orders_approve(izi_box_token, order_item_ids: list[str]):
        base_url = f'{url}/api/v1/warehouseorders/approve?showSpinner=true'

        payload = json.dumps({
            "orderItemIds": order_item_ids
        })
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

        response = requests.request("PUT", base_url, headers=headers, data=payload)
        return response

    # ორდერის მოძებნა სორტირების დეშბორდში
    @staticmethod
    def get_warehouse_orders_verified_and_failed(izi_box_token, external_id):
        base_url = f'{url}/api/v1/warehouseorders/verifiedandfailed?page=0&pageSize=25&id={external_id}&isSortOrder=false&status=55&showSpinner=true'

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

