from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.marketing_endpoint}/popups'


class PopupsEndpoints:

    @staticmethod
    def post_popups():
        return f'{base_url}'

    @staticmethod
    def get_popups():
        return f'{base_url}'

    @staticmethod
    def delete_popups_id(popups_id: int):
        return f'{base_url}/{popups_id}'

    @staticmethod
    def put_popups_id(popups_id: int):
        return f'{base_url}/{popups_id}'

    @staticmethod
    def get_admin_panel():
        return f'{base_url}/admin-panel'

    @staticmethod
    def post_upload_image():
        return f'{base_url}/upload-image'

    @staticmethod
    def post_send_email():
        return f'{base_url}/send-email'
