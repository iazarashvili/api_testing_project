from services.basket_service.wish_list.wish_list_api import WishListApi


class WishListHelpers:

    @staticmethod
    def empty_wishlist():
        wish_list_api = WishListApi()
        response = wish_list_api.get_products()
        for item in response.json()['wishlistItems']:
            response = wish_list_api.delete_remove_product(item['id'])
