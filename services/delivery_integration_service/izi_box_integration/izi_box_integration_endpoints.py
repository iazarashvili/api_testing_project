from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.izi_box_integration}'


class IziBoxIntegrationEndpoints:

    @staticmethod
    def get_webhook(event_type, status, order_line_id, order_id, my_hash):
        endpoint = (f'{base_url}webhook?EventType={event_type}&Status={status}&ExternalOrderLineId={order_line_id}'
                    f'&ExternalOrderId={order_id}&Hash={my_hash}')
        return endpoint
