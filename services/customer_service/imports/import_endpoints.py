from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.customer_endpoint}/import/timeslots'


class ImportEndpoints:

    @staticmethod
    def post_import_timeslots():
        return base_url
