from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.notification_endpoint}/devices'


class DevicesEndpoints:
    @staticmethod
    def post_register_device():
        return f'{base_url}/registerdevice'

    @staticmethod
    def post_unregister_device():
        return f'{base_url}/unregisterdevice'

    @staticmethod
    def put_change_registration_token():
        return f'{base_url}/changeregistrationtoken'

    @staticmethod
    def post_validate_token():
        return f'{base_url}/validatetoken'

    @staticmethod
    def post_register_apns_token():
        return f'{base_url}/registerapnstoken'
