from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}/feeds/atom'


class FeedsEndpoints:

    @staticmethod
    def get_feeds_atom_category_id_unpublished_date_modified_form(main_category_id, unpublished_date_modified_form):
        return f'{base_url}/{main_category_id}/{unpublished_date_modified_form}'
