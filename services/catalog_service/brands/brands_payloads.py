from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class BrandsPayload:
    correlationId: Optional[str] = None
    caption: Optional[str] = None
    logoGuid: Optional[str] = None
    status: Optional[int] = None
    ownerType: Optional[int] = None
    brandId: Optional[int] = None
    categoryId: Optional[int] = None
    featureId: Optional[int] = None
    featureValue: Optional[str] = None
    userId: Optional[str] = None
    modelId: Optional[int] = None
    brandCategoryId: Optional[int] = None

    @staticmethod
    def post_add_category(correlation_id, brand_id, category_id):
        payload = BrandsPayload(
            correlationId=correlation_id,
            brandId=brand_id,
            categoryId=category_id
        )
        return asdict(payload)

    @staticmethod
    def post_add_category_feature_value(correlation_id, brand_id, category_id, feature_id, feature_values):
        payload = BrandsPayload(
            correlationId=correlation_id,
            brandId=brand_id,
            categoryId=category_id,
            featureId=feature_id,
            featureValue=feature_values
        )
        return asdict(payload)

    @staticmethod
    def post_add_model(correlation_id, brand_id, category_id, caption, status, owner_type, user_id):
        payload = BrandsPayload(
            correlationId=correlation_id,
            brandId=brand_id,
            categoryId=category_id,
            caption=caption,
            status=status,
            ownerType=owner_type,
            userId=user_id
        )
        return asdict(payload)

    @staticmethod
    def brands_update_model(correlation_id, model_id, brand_category_id, caption, status):
        payload = BrandsPayload(
            correlationId=correlation_id,
            modelId=model_id,
            brandCategoryId=brand_category_id,
            caption=caption,
            status=status
        )
        return asdict(payload)