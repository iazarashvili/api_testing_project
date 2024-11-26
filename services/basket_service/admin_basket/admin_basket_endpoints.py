from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.basket_endpoint}adminbasket'


class AdminBasketEndpoints:
    get_admin_basket = lambda self, user_gui_id, dark_store_id=None: f'{base_url}?userId={user_gui_id}'
    post_update_basket = lambda self, user_gui_id, dark_store_id: (f'{base_url}/updatebasket?userId={user_gui_id}'
                                                                   f'&darkStoreId={dark_store_id}')
    post_remove_product = lambda self, user_gui_id, dark_store_id: (f'{base_url}/removeproduct?userId={user_gui_id}'
                                                                    f'&darkStoreId={dark_store_id}')
    post_empty_basket = lambda self, user_gui_id, dark_store_id: (f'{base_url}/emptybasket?userId={user_gui_id}'
                                                                  f'&darkStoreId={dark_store_id}')

# class AdminBasketEndpoints:
#     def __init__(self, url):
#         self.url = url
#
#     def get_admin_basket(self, user_id, dark_store_id):
#         return f'{self.url}?userId={user_id}&darkStoreId={dark_store_id}'
#
#     def post_update_basket(self, user_id, dark_store_id):
#         return f'{self.url}/updatebasket?userId={user_id}&darkStoreId={dark_store_id}'
#
#     def post_remove_product(self, user_id, dark_store_id):
#         return f'{self.url}/removeproduct?userId={user_id}&darkStoreId={dark_store_id}'
#
#     def post_empty_basket(self, user_id, dark_store_id):
#         return f'{self.url}/emptybasket?userId={user_id}&darkStoreId={dark_store_id}'
