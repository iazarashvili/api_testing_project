import uuid

from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}categories'


class CategoriesEndpoints:

    @staticmethod
    def post_check_node_categories():
        return f'{base_url}/check/node/categories'

    @staticmethod
    def get_flat():
        return f'{base_url}/flat'

    @staticmethod
    def get_as_dictionary():
        return f'{base_url}/as-dictionary'

    @staticmethod
    def get_nested():
        return f'{base_url}/nested'

    @staticmethod
    def get_categories_last_node_categories(search_value, page_number, page_size):
        return (f'{base_url}/lastnodecategories?searchValue={search_value}&'
                f'pageNumber={page_number}&pageSize={page_size}')

    @staticmethod
    def get_categories(input_str: str):
        return f'{base_url}?input={input_str}'

    @staticmethod
    def post_categories():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_categories():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def get_last_node_categories_published(search_value, page_number, page_size):
        return (f'{base_url}/lastnodecategories/published?searchValue={search_value}'
                f'&pageNumber={page_number}&pageSize={page_size}')

    @staticmethod
    def get_categories_id(category_id):
        return f'{base_url}/{category_id}'

    @staticmethod
    def get_categories_id_features(category_id):
        return f'{base_url}/{category_id}/features'

    @staticmethod
    def get_by_parent(parent_id):
        return f'{base_url}/by-parent?parentId={parent_id}'

    @staticmethod
    def get_categories_id_brands(category_id):
        return f'{base_url}/{category_id}/brands'

    @staticmethod
    def get_categories_search(search_value):
        return f'{base_url}/search?searchValue={search_value}'

    @staticmethod
    def post_add_multiple():
        # გადასახედია
        pass

    @staticmethod
    def put_categories_hide():
        return f'{base_url}/hide?requestId={uuid.uuid4()}'

    @staticmethod
    def post_add_feature():
        return f'{base_url}/addfeature?requestId={uuid.uuid4()}'

    @staticmethod
    def put_update_feature():
        return f'{base_url}/updatefeature?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_remove_feature(category_id: int, feature_id: int, correlation_id: str):
        return (f'{base_url}/removefeature?CategoryId={category_id}&FeatureId={feature_id}'
                f'&CorrelationId={correlation_id}&requestId={uuid.uuid4()}')

    @staticmethod
    def def_put_features_change_sort_indexes():
        return f'{base_url}/features/changesortindexes?requestId={uuid.uuid4()}'

    @staticmethod
    def post_sync_category_slugs():
        return f'{base_url}/synccategoryslugs'

    @staticmethod
    def post_sync_all():
        return f'{base_url}/syncall'

    @staticmethod
    def post_get_has_installment():
        return f'{base_url}/gethasinstallment'

    @staticmethod
    def get_id_feature_groups(category_id: int):
        return f'{base_url}/{category_id}'

    @staticmethod
    def put_feature_groups_change_sort_indexes():
        return f'{base_url}/featuregroups/changesortindexes?requestId={uuid.uuid4()}'

    @staticmethod
    def get_branch_by_slug(slug):
        return f'{base_url}/branch-by-slug?slug={slug}'

    @staticmethod
    def get_tree():
        return f'{base_url}/tree'

    @staticmethod
    def get_identifier_bread_crumbs(identifier: str):
        return f'{base_url}/{identifier}/breadcrumbs'

    @staticmethod
    def put_change_filters():
        return f'{base_url}/changefilters'

    @staticmethod
    def get_identifier_description(identifier):
        return f'{base_url}/{identifier}/description'

    @staticmethod
    def get_category_id_feature_values(category_id: int, page_size: int, page_number: int):
        return f'{base_url}/{category_id}/featurevalues?pageSize={page_size}&pageNumber={page_number}'

    @staticmethod
    def get_category_id_feature_values_count(category_id: int):
        return f'{base_url}/{category_id}/featurevalues/count'

    @staticmethod
    def get_children(category_id: int):
        return f'{base_url}/children?categoryId={category_id}'

    @staticmethod
    def get_main_merchant(merchant_id: int):
        return f'{base_url}/main/merchant?merchantId={merchant_id}'

    @staticmethod
    def get_merchant_last_node(merchant_id: int, search_value: str):
        return f'{base_url}/merchant/last-node?merchantId={merchant_id}&searchValur={search_value}'

    @staticmethod
    def get_merchants():
        return f'{base_url}/merchants'
