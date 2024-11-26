import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/timeslot'


class TimeSlotEndpoints:

    @staticmethod
    def post_timeslot():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_timeslot():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def get_timeslot():
        return base_url
