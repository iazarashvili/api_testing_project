class WishListPayload:

    @staticmethod
    def post_add_product(product_id):
        payload = {
            "productId": product_id
        }
        return payload
