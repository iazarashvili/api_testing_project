from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.customer_endpoint}/merchant'


class MerchantEndpoints:

    @staticmethod
    def post_merchant_timeslot():
        return f'{base_url}/timeslot'

    @staticmethod
    def put_merchant_cutoff_time():
        return f'{base_url}/cutofftime'

    @staticmethod
    def get_merchant_timeslot_details():
        return f'{base_url}/timeslot-details'
