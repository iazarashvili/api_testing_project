import uuid

from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/campaign'


class CampaignEndpoints:
    @staticmethod
    def post_register_campaign():
        return f'{base_url}/registercampaign?requestId={uuid.uuid4()}'

    @staticmethod
    def post_edit_campaign():
        return f'{base_url}/editcampaign?requestId={uuid.uuid4()}'

    @staticmethod
    def post_change_campaign_status():
        return f'{base_url}/changecampaignstatus?requestId={uuid.uuid4()}'

    @staticmethod
    def post_add_campaign_product():
        return f'{base_url}/addcampaignproduct?requestId={uuid.uuid4()}'

    @staticmethod
    def post_delete_campaign_product():
        return f'{base_url}/deletecampaignproduct?requestId={uuid.uuid4()}'

    @staticmethod
    def post_add_cashback():
        return f'{base_url}/addcashback?requestId={uuid.uuid4()}'

    @staticmethod
    def post_update_cashback():
        return f'{base_url}/updatecashback?requestId={uuid.uuid4()}'

    @staticmethod
    def post_add_multiple_campaign_product():
        return f'{base_url}/addmultiplecampaignproduct'

    @staticmethod
    def get_campaigns():
        return f'{base_url}/getcampaigns'

    @staticmethod
    def get_campaign_details():
        return f'{base_url}/getcampaigndetails'

    @staticmethod
    def get_campaign_products():
        return f'{base_url}/getcampaignproducts'

    @staticmethod
    def post_get_campaign_for_basket_product_ids():
        return f'{base_url}/getcampaignforbasket/productids'

    @staticmethod
    def get_campaign_information():
        return f'{base_url}/getcampaigninformation'

    @staticmethod
    def get_cashback_details():
        return f'{base_url}/getcashbackdetails'

    @staticmethod
    def get_active_campaigns():
        return f'{base_url}/active/campaigns'
