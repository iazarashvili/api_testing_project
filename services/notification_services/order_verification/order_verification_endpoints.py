from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.notification_endpoint}/orderverification'


class OrderVerificationEndpoints:

    @staticmethod
    def get_order_verification_otp():
        return f'{base_url}/otp'

    @staticmethod
    def put_order_verification_verify():
        return f'{base_url}/verify'
