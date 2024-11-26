import uuid
from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}'


class BrandsEndpoints:

    @staticmethod
    def get_brands(search_value, page_number, page_size):
        return f'{base_url}brands?searchValue={search_value}&pageNumber={page_number}&pageSize={page_size}'

    post_brands = f'{base_url}brands?requestId={uuid.uuid4()}'
    put_brands = f'{base_url}brands?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_brands(brand_id: int, correlation_id: str):
        return f'{base_url}brands?id={brand_id}&CorrelationId={correlation_id}&requestId={uuid.uuid4()}'

    @staticmethod
    def get_brand_id_feature_values(brand_id):
        return f'{base_url}brands/{brand_id}/featurevalues'

    @staticmethod
    def get_brand_id_categories_category_id_models(brand_id, category_id, status):
        return f'{base_url}brands/{brand_id}/categories/{category_id}/models?status={status}'

    @staticmethod
    def get_brands_by_category_id_category_id(category_id):
        return f'{base_url}brands/getbrandsbycategoryid/{category_id}'

    @staticmethod
    def get_models_by_brand_id_brand_id_category_id(brand_id, category_id):
        return f'{base_url}brands/getmodelbybrandid/{brand_id}/{category_id}'

    @staticmethod
    def get_brand_id_categories(brand_id):
        return f'{base_url}brands/{brand_id}/categories'

    @staticmethod
    def get_brands_id(id):
        return f'{base_url}brands/{id}'

    @staticmethod
    def post_add_category():
        return f'{base_url}brands/addcategory?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_remove_category(brand_id, category_id, correlation_id):
        return f'{base_url}brands/removecategory?brandId={brand_id}&CategoryId={category_id}&CorrelationId={correlation_id}'

    @staticmethod
    def post_add_category_feature_value():
        return f'{base_url}brands/addcategoryfeaturevalue?requestId={uuid.uuid4()}'

    @staticmethod
    def put_update_category_feature_value():
        return f'{base_url}brands/updatecategoryfeaturevalue?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_remove_category_feature_value(feature_suggested_value_id, correlation_id):
        return (
            f'{base_url}brands/removecategoryfeaturevalue?FeatureSuggestedValueId={feature_suggested_value_id}&CorrelationId={correlation_id}'
            f'&requestId={uuid.uuid4()}')

    @staticmethod
    def post_add_model():
        return f'{base_url}brands/addmodel?requestId={uuid.uuid4()}'

    @staticmethod
    def put_update_model():
        return f'{base_url}brands/updatemodel?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_remove_model(brand_category_id, model_id, correlation_id):
        return (f'{base_url}brands/removemodel?BrandCategoryId={brand_category_id}&ModelId={model_id}'
                f'&CorrelationId={correlation_id}')