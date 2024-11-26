from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class GeneratePromoCode:
    correlationId: Optional[str] = None
    companyName: Optional[str] = None
    code: Optional[str] = None
    promoValue: Optional[int] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    useType: Optional[int] = None
    cartLimit: Optional[int] = None
    promoType: Optional[int] = None
    promoChannel: Optional[int] = None
    promoTarget: Optional[int] = None
    cap: Optional[int] = None
    userCategory: Optional[int] = None
    includeDeliveryPrice: Optional[bool] = None
    numberOfOrders: Optional[int] = None
    isReferrerType: Optional[bool] = None


@dataclass
class UpdatePromoCode:
    correlationId: Optional[str] = None
    promoCodeId: Optional[int] = None
    endDate: Optional[datetime] = None
    cartLimit: Optional[int] = None
    promoChannel: Optional[int] = None
    cap: Optional[int] = None
    isReferrerType: Optional[bool] = None


@dataclass
class ChangePromoCodeStatus:
    correlationId: Optional[str] = None
    promoCodeId: Optional[int] = None
    status: Optional[int] = None


@dataclass
class AddMultiplePromoCode:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class Products:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ProductsDelete:
    productIds: Optional[List[int]]
