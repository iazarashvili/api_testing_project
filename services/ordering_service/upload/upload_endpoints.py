import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/upload'


class UploadEndpoints:

    @staticmethod
    def post_upload_image():
        return base_url
