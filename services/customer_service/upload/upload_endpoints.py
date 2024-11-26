from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.customer_endpoint}/upload'


class UploadEndpoints:

    @staticmethod
    def post_upload_document():
        return f'{base_url}/document'

    @staticmethod
    def post_upload_image():
        return f'{base_url}/image'

    @staticmethod
    def post_upload_cover_image():
        return f'{base_url}/coverimage'

    @staticmethod
    def post_upload_size_guide_pdf():
        return f'{base_url}/sizeguidepdf'

    @staticmethod
    def post_upload_guarantee():
        return f'{base_url}/guarantee'
