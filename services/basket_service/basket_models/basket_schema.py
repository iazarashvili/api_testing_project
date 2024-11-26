from typing import List, Optional, Union
from pydantic import BaseModel, field_validator
from utils.enums.product_status_enums import PublicEnumProductStatus


class ProductDetail(BaseModel):
    key: str
    value: str


class Product(BaseModel):
    productId: int
    productCount: int
    price: float
    title: str
    imageUrl: str
    discountedPrice: Optional[Union[float, None]]
    discountedPercent: Optional[Union[float, None]]
    commercialTitle: str
    quantity: int
    isPreOrderProduct: Optional[bool]
    productStatus: int
    customerId: str
    details: Optional[List[ProductDetail]]
    discountType: int
    discountValue: Optional[float]
    valueType: Optional[str]
    categorySlug: str
    productSlug: str
    productOriginalSlug: str
    sellerSlug: str
    sellerId: int
    isExpress: bool
    darkStoreId: Optional[int]
    sku: Optional[Union[str, None]]
    isActive: bool

    @field_validator('productStatus')
    def product_status_is_not_unpublished(cls, value):
        if value != PublicEnumProductStatus.Published or value is None:
            raise ValueError('Item is not published')
        else:
            return value

    @field_validator('productId', 'productCount', 'price',
                     'title', 'imageUrl', 'commercialTitle', 'customerId', 'categorySlug',
                     'quantity', 'customerId', 'productSlug', 'productOriginalSlug', 'sellerSlug', 'sellerId')
    def quantity_is_not_null(cls, value):
        if value == "" and value is None:
            raise ValueError('Item quantity equal 0')
        else:
            return value


class BasketSchema(BaseModel):
    data: List[Product]
    totalPrice: float
    quantityFailed: bool
