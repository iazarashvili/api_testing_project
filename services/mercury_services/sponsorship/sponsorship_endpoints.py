from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.mercury_endpoint}'


class SponsorshipsEndpoints:

    @staticmethod
    def post_ids(ids: list):
        return f'{base_url}{ids}'
