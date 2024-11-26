import requests
import allure

from services.ordering_service.campaign.campaing_endpoints import CampaignEndpoints
from config.headers import Headers


class CampaignApi:
    def __init__(self):
        super().__init__()
        self._endpoints = CampaignEndpoints()
        self._headers = Headers()

    def post_register_campaign(self, payload):
        response = requests.post(
            url=self._endpoints.post_register_campaign(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_edit_campaign(self, payload):
        response = requests.post(
            url=self._endpoints.post_edit_campaign(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_change_campaign_status(self, payload):
        response = requests.post(
            url=self._endpoints.post_change_campaign_status(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_add_campaign_product(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_campaign_product(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_delete_campaign_product(self, payload):
        response = requests.post(
            url=self._endpoints.post_delete_campaign_product(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_add_cash_back(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_cashback(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_update_cash_back(self, payload):
        response = requests.post(
            url=self._endpoints.post_update_cashback(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def post_add_multiple_campaign_product(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_multiple_campaign_product(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_campaigns(self, params):
        response = requests.get(
            url=self._endpoints.get_campaigns(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_campaign_details(self):
        response = requests.get(
            url=self._endpoints.get_campaign_details(),
            headers=self._headers.cms_token
        )
        return response

    def get_campaign_products(self, params):
        response = requests.get(
            url=self._endpoints.get_campaign_products(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def post_campaign_for_basket_product_ids(self, payload: list):
        response = requests.post(
            url=self._endpoints.post_get_campaign_for_basket_product_ids(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_campaign_information(self, params):
        response = requests.get(
            url=self._endpoints.get_campaign_information(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_cashback_details(self, params):
        response = requests.get(
            url=self._endpoints.get_cashback_details(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def get_active_campaigns(self):
        response = requests.get(
            url=self._endpoints.get_active_campaigns(),
            headers=self._headers.cms_token
        )
        return response
