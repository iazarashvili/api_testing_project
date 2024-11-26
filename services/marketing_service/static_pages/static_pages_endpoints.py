from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.marketing_endpoint}/staticpages'


class StaticPagesEndpoints:

    @staticmethod
    def post_create_static_page():
        return f'{base_url}/createstaticpage'

    @staticmethod
    def delete_remove_static_page():
        return f'{base_url}/removestaticpage'

    @staticmethod
    def get_static_pages():
        return f'{base_url}/static-pages'

    @staticmethod
    def put_update_static_page():
        return f'{base_url}/updatestaticpage'

    @staticmethod
    def get_static_page_details():
        return f'{base_url}/static-page-details'

    @staticmethod
    def post_create_static_page_group():
        return f'{base_url}/createstaticpagegroup'

    @staticmethod
    def delete_remove_static_page_group():
        return f'{base_url}/removestaticpagegroup'

    @staticmethod
    def get_remove_static_page_group():
        return f'{base_url}/static-page-groups'

    @staticmethod
    def get_static_page_groups_for_dropdown():
        return f'{base_url}/getstaticpagegroupsfordropdown'

    @staticmethod
    def put_update_static_page_group():
        return f'{base_url}/updatestaticpagegroup'

    @staticmethod
    def get_static_page_group_details():
        return f'{base_url}/static-page-group-details'

    @staticmethod
    def get_static_pages_and_groups():
        return f'{base_url}/static-pages-and-groups'

    @staticmethod
    def get_static_page_description():
        return f'{base_url}/static-page-description'
