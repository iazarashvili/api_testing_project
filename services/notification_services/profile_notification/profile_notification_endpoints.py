from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.notification_endpoint}/profilenotification'


class ProfileNotificationEndpoints:

    @staticmethod
    def get_profile_notification():
        return f'{base_url}'

    @staticmethod
    def post_profile_notification():
        return base_url

    @staticmethod
    def patch_profile_notification_id_status(any_id: str):
        return f'{base_url}/{any_id}/status'
