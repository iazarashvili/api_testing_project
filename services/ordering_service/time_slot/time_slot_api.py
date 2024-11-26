import requests
import allure

from services.ordering_service.time_slot.time_slot_endpoints import TimeSlotEndpoints
from config.headers import Headers


class TimeslotApi:

    def __init__(self):
        super().__init__()
        self._endpoints = TimeSlotEndpoints()
        self._headers = Headers()

    def post_timeslot(self, payload):
        response = requests.post(
            url=self._endpoints.post_timeslot(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_timeslot(self, payload):
        response = requests.put(
            url=self._endpoints.put_timeslot(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_timeslot(self, params):
        response = requests.get(
            url=self._endpoints.get_timeslot(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
