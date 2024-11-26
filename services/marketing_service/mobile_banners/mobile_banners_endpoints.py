from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.marketing_endpoint}/mobilebanners'


class MobileBannersEndpoints:

    @staticmethod
    def get_mobile_banners():
        return f'{base_url}'

    @staticmethod
    def get_mobile_banners_landing_banners():
        return f'{base_url}/landing-banners'

    @staticmethod
    def get_mobile_banners_advertisement_banners():
        return f'{base_url}/advertisement-banners'
