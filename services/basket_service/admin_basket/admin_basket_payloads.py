class AdminBasketPayloads:

    @staticmethod
    def post_update_basket(product_id, product_count):
        payload = {
            "productId": product_id,
            "productCount": product_count,
            "details": []
        }
        return payload

    @staticmethod
    def post_remove_products(product_id, dark_store_id):
        payload = {
            "productId": product_id,
            "darkStoreId": dark_store_id
        }
        return payload
