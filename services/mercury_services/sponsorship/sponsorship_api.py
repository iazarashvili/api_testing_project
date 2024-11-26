import requests

from services.mercury_services.sponsorship.sponsorship_endpoints import SponsorshipsEndpoints


class SponsorshipsApi:

    def __init__(self):
        super().__init__()
        self.endpoints = SponsorshipsEndpoints()

    def post_sponsorships_ids(self, ids: list):
        response = requests.post(
            url=self.endpoints.post_ids(ids)
        )
        return response
