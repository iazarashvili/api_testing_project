import requests
import allure

from services.ordering_service.upload.upload_endpoints import UploadEndpoints
from config.headers import Headers


class UploadApi:

    def __init__(self):
        super().__init__()
        self._endpoints = UploadEndpoints()
        self._headers = Headers()

    def post_upload_image(self, file):
        response = requests.post(
            url=self._endpoints.post_upload_image(),
            params=file,
            headers=self._headers.web_token
        )
        return response
