from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class Product(BaseModel):
    id: int
    imageUrl: HttpUrl
    imageName: str
    title: str
    productSlug: str
    productOriginalSlug: str
    categorySlug: str
    categoryOriginalSlug: str
    sellerName: str
    sellPrice: float
    discountPercent: Optional[float]
    discountedPrice: Optional[float]
    discountPeriodStartDate: Optional[str]
    discountPeriodEndDate: Optional[str]
    hasGift: Optional[bool]
    ageContentRestriction: bool
    status: int
    quantity: Optional[int]
    hasInstallment: bool
    merchantHasInstallment: bool
    monthlyPayment: Optional[float]
    sellerSlug: str
    sellerId: int
    showDiscountTimer: bool
    categoryId: int
    isSponsored: Optional[bool]
    isExpress: bool
    darkStoreId: Optional[int]


class ProductsSchema(BaseModel):
    data: List[Product]
    hasAgeContentRestriction: bool
