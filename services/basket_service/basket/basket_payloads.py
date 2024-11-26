import json


class BasketPayload:

    @staticmethod
    def update_basket_multiple_payload():
        payload = {
            "basketItems": [
                {
                    "productId": 0,
                    "productCount": 0,
                    "details": [
                        {
                            "key": "string",
                            "value": "string"
                        }
                    ]
                },
            ],
            "darkStoreId": 0
        }
        return payload

    @staticmethod
    def update_basket_payload(item_id, item_json, count, dark_store_id):
        payload = {
            "basket": {
                "productId": item_id,
                "discountType": item_json,
                "productCount": count,
                "type": "[BASKET] UpdateBasket"
            },
            "darkStoreId": dark_store_id
        }
        return payload

    @staticmethod
    def post_empty_basket_payload(dark_store_id):
        payload = {
            "darkStoreId": dark_store_id
        }
        return payload

    @staticmethod
    def post_remove_product_payload(product_id, dark_store_id=0):
        payload = {
            "productId": product_id,
            "darkStoreId": dark_store_id
        }
        return payload

    @staticmethod
    def post_update_basket_products(product_id, product_count, dark_store_id=0):
        payload = {
            "basketItems": [
                {
                    "productId": product_id,
                    "productCount": product_count,
                    "details": [
                        {
                            "key": "string",
                            "value": "string"
                        }
                    ]
                }
            ],
            "darkStoreId": dark_store_id
        }
        return payload

    @staticmethod
    def post_update_basket_express_products(dark_store_id):
        payload = {
            "darkStoreId": dark_store_id
        }
        return payload
