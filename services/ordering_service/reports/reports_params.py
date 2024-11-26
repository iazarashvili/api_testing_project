from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class Orders:
    From: Optional[datetime] = None
    To: Optional[datetime] = None


@dataclass
class OrderItems:
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    MerchantName: Optional[str] = None
    ProductTitle: Optional[str] = None
    OrderId: Optional[int] = None
    CreatedFrom: Optional[datetime] = None
    CreatedTo: Optional[datetime] = None
    OrderLineStatus: Optional[int] = None
    Reservist: Optional[str] = None
    OrderLineGeneralStatus: Optional[int] = None
    ShippingOptionId: Optional[int] = None
    OrderGeneralStatus: Optional[int] = None
    ReservationStatus: Optional[List[int]] = None
    DeliveryStatus: Optional[int] = None
    IsFirstOrder: Optional[float] = None
    DeliveryDateFrom: Optional[datetime] = None
    DeliveryDateTo: Optional[datetime] = None
    SubOrderId: Optional[str] = None


@dataclass
class ShippingPackages:
    LocationId: Optional[int] = None
    ShippingPackageSizeId: Optional[int] = None
    Limit: Optional[float] = None
    Amount: Optional[float] = None
