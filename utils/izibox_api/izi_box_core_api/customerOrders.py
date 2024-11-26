import json
import uuid
import requests

url = None


class CustomerOrders:
    @staticmethod
    def post_customer_orders_order_items_package_size(izi_box_token, order_item_ids: list[str]):
        base_url = f'{url}/api/v1/customerorders/orderitems/packagesize?showSpinner=true'
        payload = json.dumps({
            "packageSizeName": "M",
            "orderItemIds": order_item_ids
        })
        headers = {
            'authority': 'core-api.staging.izibox.ge',
            'accept': 'application/json, text/plain, */*',
            'authorization': 'Bearer ' + izi_box_token,
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://dashboard.staging.izibox.ge',
            'pragma': 'no-cache',
            'referer': 'https://dashboard.staging.izibox.ge/',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'x-requestid': str(uuid.uuid4())
        }

    @staticmethod
    def get_customer_orders_order_id(izi_box_token, external_id):
        base_url = f'{url}/api/v1/customerorders?orderId={external_id}&page=0&pageSize=20&showSpinner=true'

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
