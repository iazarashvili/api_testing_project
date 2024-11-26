import requests
import allure

from services.customer_service.upload.upload_endpoints import UploadEndpoints
from config.headers import Headers


class UploadApi:
    def __init__(self):
        super().__init__()
        self._endpoints = UploadEndpoints()
        self._headers = Headers()

    def upload_document(self, files):
        response = requests.post(
            url=self._endpoints.post_upload_document(),
            files=files,
            headers=self._headers.cms_token
        )
        return response

    def upload_image(self, file):
        response = requests.post(
            url=self._endpoints.post_upload_image(),
            files=file,
            headers=self._headers.cms_token
        )
        return response

    def upload_cover_image(self, files):
        """
        :param files: files = [('file', ('file', open('Screenshot_6.png', 'rb'), 'application/octet-stream'))]
        """
        response = requests.post(
            url=self._endpoints.post_upload_cover_image(),
            files=files,
            headers=self._headers.cms_token
        )
        return response

    def upload_size_guide(self, file):
        response = requests.post(
            url=self._endpoints.post_upload_size_guide_pdf(),
            files=file,
            headers=self._headers.cms_token
        )
        return response

    def upload_size_guarantee(self, file):
        response = requests.post(
            url=self._endpoints.post_upload_guarantee(),
            files=file,
            headers=self._headers.cms_token
        )
        return response
