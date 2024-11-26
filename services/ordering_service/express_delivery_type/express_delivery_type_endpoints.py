import uuid

from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/expressdeliverytype'


class ExpressDeliveryTypeEndpoints:

    @staticmethod
    def post_express_delivery_type():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def get_express_delivery_type():
        return base_url
