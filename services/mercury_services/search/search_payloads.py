from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Gogo:
    searchText: Optional[str] = None


@dataclass
class BillieJaneData:
    additionalProp1: Optional[List[str]] = None


@dataclass
class BillieJean:
    searchText: Optional[str] = None
    categorySlug: Optional[str] = None
    categoryId: Optional[int] = None
    setIds: Optional[List[int]] = None
    merchantSlugs: Optional[List[str]] = None
    userSlug: Optional[str] = None
    merchantId: Optional[int] = None
    brandIds: Optional[List[int]] = None
    modelIds: Optional[List[int]] = None
    features: Optional[List[BillieJaneData]] = None
    priceFrom: Optional[int] = None
    priceTo: Optional[int] = None
    filterByDiscount: Optional[bool] = None
    filterByGift: Optional[bool] = None
    darkStoreId: Optional[int] = None
    deliveryTypes: Optional[int] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    merchantNameStartsWith: Optional[str] = None
    merchantsSearchText: Optional[str] = None
    sortType: Optional[int] = None
    sortBy: Optional[int] = None


@dataclass
class CoolCat:
    searchText: Optional[str] = None
    userSlug: Optional[str] = None
    merchantId: Optional[int] = None
    darkStoreId: Optional[int] = None
    deliveryTypes: Optional[int] = None


@dataclass
class MammaMia:
    searchText: Optional[str] = None
    searchImageId: Optional[str] = None
    userSlug: Optional[str] = None
    merchantId: Optional[int] = None
    darkStoreId: Optional[int] = None
    deliveryTypes: Optional[int] = None


@dataclass
class Sunny:
    merchantNameStartsWith: Optional[str] = None
    categoryId: Optional[int] = None
    searchText: Optional[str] = None
