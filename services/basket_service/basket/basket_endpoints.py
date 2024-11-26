import uuid

# url = "https://basket.dev.extra.ge/v1" if os.environ["STAGE"] == "qa" else "https://basket.staging.extra.ge/v1"
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.basket_endpoint}basket'


class BasketEndpoints:
    get_basket = f'{base_url}'
    post_basket_for_anonymous_user = base_url
    post_update_basket_multiple = f'{base_url}/updatebasketmultiple'

    @staticmethod
    def post_update_basket():
        post_update_basket = f'{base_url}/updatebasket?requestId={uuid.uuid4()}'
        return post_update_basket

    post_empty_basket = f'{base_url}/emptybasket'
    post_remove_product = f'{base_url}/removeproduct?requestId={uuid.uuid4()}'
    post_update_basket_products = f'{base_url}/updatebasketproducts?requestId={uuid.uuid4()}'
    post_update_basket_express_products = f'{base_url}/updatebasketexpressproducts'
