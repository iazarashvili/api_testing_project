from dataclasses import dataclass, field, asdict
from typing import Optional, List


@dataclass
class EmployeeProfileGet:
    SearchValue: Optional[str] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None


@dataclass
class Orders:
    SearchValue: Optional[str] = None
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    Status: Optional[List[int]] = None
    PersonalNumber: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PaymentType: Optional[List[int]] = None
    PriceFrom: Optional[float] = None
    PriceTo: Optional[float] = None
    CreateTimeFrom: Optional[str] = None
    CreateTimeTo: Optional[str] = None
    PromoCode: Optional[str] = None
    DeliveryType: Optional[List[int]] = None
    CampaignId: Optional[int] = None
    ReferrerType: Optional[int] = None
    ShippingOptionId: Optional[int] = None
    OrderId: Optional[int] = None
    OrderGeneralStatus: Optional[List[int]] = None
    OrderCancellationReason: Optional[List[int]] = None
    IsFirstOrder: Optional[bool] = None
    ContainsOutOfStockOrderItem: Optional[bool] = None
    ContainsExternalFailedOrderLine: Optional[bool] = None
    OwnerEmployee: Optional[str] = None
    SortBy: Optional[int] = None
