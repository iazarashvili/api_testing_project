import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/promocodes'


class PromoCodesEndpoints:

    @staticmethod
    def post_generate_promo_code():
        return f'{base_url}/generatepromocode?requestId={uuid.uuid4()}'

    @staticmethod
    def put_update_promo_code():
        return f'{base_url}/updatepromocode?requestId={uuid.uuid4()}'

    @staticmethod
    def put_change_promo_code_status():
        return f'{base_url}/changepromocodestatus?requestId={uuid.uuid4()}'

    @staticmethod
    def post_add_multiple_promo_code():
        return f'{base_url}/addmultiplepromocode?requestId={uuid.uuid4()}'

    @staticmethod
    def post_id_products(promo_id: int):
        return f'{base_url}/{promo_id}/products?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_id_products(product_id: int):
        return f'{base_url}/{product_id}/products?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_id_products_clear(product_id: int):
        return f'{base_url}/{product_id}/products/clear?requestId={uuid.uuid4()}'

    @staticmethod
    def get_promo_code_details_promo_code_id(promo_code_id: int):
        return f'{base_url}/promocode-details/{promo_code_id}'

    @staticmethod
    def get_promo_code_validation_promo_code(promo_code: str):
        return f'{base_url}/promocode-validation/{promo_code}'

    @staticmethod
    def get_promo_codes():
        return f'{base_url}/getpromocodes'

    @staticmethod
    def get_id_products(promo_code_id: int):
        return f'{base_url}/{promo_code_id}/products'
