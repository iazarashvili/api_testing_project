from typing import List, Optional
from pydantic import BaseModel, field_validator

from utils.enums.product_status_enums import PublicEnumProductStatus


class WishlistItem(BaseModel):
    id: int
    imageUrl: str
    title: str
    productSlug: str
    productOriginalSlug: str
    categorySlug: str
    sellerName: str
    sellPrice: float
    discountPercent: Optional[float]
    discountedPrice: Optional[float]
    discountPeriodStartDate: Optional[str]
    discountPeriodEndDate: Optional[str]
    hasGift: Optional[bool]
    status: int
    monthlyPayment: Optional[float]
    sellerId: int
    sellerSlug: str
    isExpress: bool
    darkStoreId: Optional[int]
    sku: Optional[str]
    isActive: bool

    @field_validator('isActive')
    def product_status_is_not_unpublished(cls, value):
        assert value is True, 'Item is not active'

    @field_validator('status')
    def status_is_active(cls, status):
        assert status == 1, 'status is not active'


class WishlistSchema(BaseModel):
    wishlistItems: List[WishlistItem]
    totalCount: int
