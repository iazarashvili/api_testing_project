from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.customer_endpoint}/referral'


class ReferralEndpoints:

    @staticmethod
    def post_referral():
        return f'{base_url}'

    @staticmethod
    def put_referral():
        return f'{base_url}'

    @staticmethod
    def get_referral():
        return f'{base_url}'

    @staticmethod
    def post_referral_add_milestone():
        return f'{base_url}/addmilestone'

    @staticmethod
    def put_referral_update_milestone():
        return f'{base_url}updatemilestone'

    @staticmethod
    def delete_remove_milestone_milestone_id(milestone_id):
        return f'{base_url}/removemilestone/{milestone_id}'

    @staticmethod
    def post_receive_milestone():
        return f'{base_url}/receivemilestone'

    @staticmethod
    def post_add_verified_customer_referral():
        return f'{base_url}/addverifiedcustomerreferral'

    @staticmethod
    def get_customer_benefits_admin():
        return f'{base_url}/customer-benefits-admin'

    @staticmethod
    def get_customer_benefits_admin_id(referral_id):
        return f'{base_url}/customer-benefits-admin/{referral_id}'

    @staticmethod
    def get_customer_benefits():
        return f'{base_url}/customer-benefits'
