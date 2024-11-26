from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.marketing_endpoint}/section'


class SectionEndpoints:

    @staticmethod
    def post_create_section():
        return f'{base_url}/createsection'

    @staticmethod
    def put_change_section():
        return f'{base_url}/changesection'

    @staticmethod
    def get_sections():
        return f'{base_url}/sections'

    @staticmethod
    def get_sections_admin():
        return f'{base_url}/sections-admin'

    @staticmethod
    def get_section_details():
        return f'{base_url}/section-details'

    @staticmethod
    def post_upload_image():
        return f'{base_url}/uploadimage'

    @staticmethod
    def put_sort_index():
        return f'{base_url}/sort-index'

    @staticmethod
    def delete_image():
        return f'{base_url}/image'

    @staticmethod
    def delete_section():
        return f'{base_url}/section'
