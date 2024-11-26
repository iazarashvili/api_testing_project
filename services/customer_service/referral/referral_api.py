import allure
import requests

from services.customer_service.referral.referral_endpoints import ReferralEndpoints
from config.headers import Headers


class ReferralApi:

    def __init__(self):
        super().__init__()
        self._endpoints = ReferralEndpoints()
        self._headers = Headers()

    def post_referral(self, payload):
        response = requests.post(
            url=self._endpoints.post_referral(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_referral(self, payload):
        response = requests.put(
            url=self._endpoints.put_referral(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_referral(self):
        response = requests.get(
            url=self._endpoints.get_referral(),
            headers=self._headers.cms_token
        )
        return response

    def post_add_milestone(self, payload):
        response = requests.post(
            url=self._endpoints.post_referral_add_milestone(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_update_milestone(self, payload):
        response = requests.put(
            url=self._endpoints.put_referral_update_milestone(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def delete_remove_milestone_milestone_id(self, milestone_id):
        response = requests.delete(
            url=self._endpoints.delete_remove_milestone_milestone_id(milestone_id),
            headers=self._headers.cms_token
        )
        return response

    def post_receive_milestone(self, payload):
        response = requests.post(
            url=self._endpoints.post_receive_milestone(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_add_verified_customer_referral(self, payload=None):
        response = requests.post(
            url=self._endpoints.post_add_verified_customer_referral(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_customer_benefits_admin(self, params):
        response = requests.get(
            url=self._endpoints.get_customer_benefits_admin(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_customer_benefits_admin_id(self, customer_id: int):
        response = requests.get(
            url=self._endpoints.get_customer_benefits_admin_id(customer_id),
            headers=self._headers.cms_token
        )
        return response

    def get_customer_benefits(self):
        response = requests.get(
            url=self._endpoints.get_customer_benefits(),
            headers=self._headers.cms_token
        )
        return response
