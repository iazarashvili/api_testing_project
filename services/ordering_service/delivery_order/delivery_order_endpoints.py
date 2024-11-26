import uuid

from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/deliveryorder'


class DeliveryOrderEndpoints:
    @staticmethod
    def put_change_delivery_order_status():
        return f'{base_url}/change-deliveryorder-status?requestId={uuid.uuid4()}'
