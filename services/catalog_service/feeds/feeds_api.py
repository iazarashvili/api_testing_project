import allure
import requests

from services.catalog_service.feeds.feeds_endpoints import FeedsEndpoints
from config.headers import Headers


class FeedsApi:

    def __init__(self):
        super().__init__()
        self._endpoints = FeedsEndpoints()
        self._headers = Headers()

    @allure.step('Get feeds atom main category id unpublished date modified form')
    def get_feeds_atom_category_id_unpublished_date_modified_form(self, main_category_id, unpublished_date_modified_form):
        response = requests.get(
            url=self._endpoints.get_feeds_atom_category_id_unpublished_date_modified_form(main_category_id, unpublished_date_modified_form),
            headers=self._headers.cms_token
        )
        return response
