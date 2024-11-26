from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class OrderReservation:
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    OrderExternalId: Optional[int] = None
    ProductId: Optional[int] = None
    ProductTitle: Optional[str] = None
    MerchantId: Optional[str] = None
    FromOrderDate: Optional[str] = None
    ToOrderDate: Optional[str] = None
    ReservationStatus: Optional[list[int]] = None
    FromDeliveryDate: Optional[str] = None
    ToDeliveryDate: Optional[str] = None


@dataclass
class OrderReservationStatusCount:
    merchantId: Optional[str] = None
    categoryIds: Optional[List[int]] = field(default_factory=list)


@dataclass
class ReservationOrderLineStatusChangeHistories:
    OrderLineId: Optional[int]
