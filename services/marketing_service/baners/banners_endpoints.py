from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.marketing_endpoint}/banners'


class BannersEndpoints:

    @staticmethod
    def post_create_banner_place():
        return f'{base_url}/createbannerplace'

    @staticmethod
    def delete_delete_banner_place():
        return f'{base_url}/deletebannerplace'

    @staticmethod
    def get_banner_places():
        return f'{base_url}/bannerplaces'

    @staticmethod
    def get_banner_place_details():
        return f'{base_url}/bannerplace-details'

    @staticmethod
    def post_add_banner():
        return f'{base_url}/addbanner'

    @staticmethod
    def post_change_banner_status():
        return f'{base_url}/changebannerstatus'

    @staticmethod
    def put_update_banner_sort_index():
        return f'{base_url}/updatebannersortindex'

    @staticmethod
    def delete_remove_banner():
        return f'{base_url}/removebanner'

    @staticmethod
    def post_upload_banner_image():
        return f'{base_url}/uploadbannerimage'

    @staticmethod
    def get_ribbon():
        return f'{base_url}/ribbon'

    @staticmethod
    def put_update_banner():
        return f'{base_url}/updatebanner'

    @staticmethod
    def get_dynamic_banner_place():
        return f'{base_url}/dynamic-bannerplace'

    @staticmethod
    def put_change_banner_place_owner():
        return f'{base_url}/change-bannerplace-owner'

    @staticmethod
    def get_details():
        return f'{base_url}/details'

    @staticmethod
    def get_dynamic_banner_places():
        return f'{base_url}/dynamic-bannerplaces'
