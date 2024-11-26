from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class PromoCodeValidationPromoCode:
    orderReferrerType: Optional[int] = None
    cartAmount: Optional[float] = None


@dataclass
class GetPromoCodes:
    Status: Optional[int] = None
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    SearchValue: Optional[str] = None
    CompanyName: Optional[str] = None
    Code: Optional[str] = None
    UseCount: Optional[str] = None
    UseType: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PromoType: Optional[int] = None
    PromoChannel: Optional[int] = None
    PromoTarget: Optional[int] = None
    UserCategory: Optional[int] = None


@dataclass
class IdProducts:
    ProductId: Optional[int] = None
    PageSize: Optional[int] = None
    PageNumber: Optional[int] = None
