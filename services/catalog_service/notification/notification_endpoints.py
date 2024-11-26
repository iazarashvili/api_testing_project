from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}/notification/sendfeatureaddmail'


class NotificationEndpoints:

    @staticmethod
    def post_send_feature_add_mail():
        return base_url
