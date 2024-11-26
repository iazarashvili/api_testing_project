from utils.data.endpoints_data import Endpoints
import uuid

base_url = f'{Endpoints.catalog_endpoint}advertisements'


class AdvertisementsEndpoints:
    get_advertisements = base_url
    post_advertisements = f'{base_url}?requestId={uuid.uuid4()}'
    put_advertisements = f'{base_url}?requestId={uuid.uuid4()}'
    delete_advertisements = f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def get_id(id):
        endpoint = f'{base_url}{id}'
        return endpoint

    @staticmethod
    def get_id_categories(id):
        endpoint = f'{base_url}{id}/categories'
        return endpoint

    @staticmethod
    def get_brand_logos_by_category(category_slug):
        endpoint = f'https://catalog.staging.extra.ge/api/brand-logos/by-category?categorySlug={category_slug}'
        return endpoint

    post_update_categories = f'{base_url}update-categories{uuid.uuid4()}'
