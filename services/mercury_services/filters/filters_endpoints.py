from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.mercury_endpoint}/filters'


class FiltersEndpoint:
    @staticmethod
    def post_beat_it():
        return f'{base_url}/beat-it'
