from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class OrderReservationItemExcel:
    MerchantId: Optional[str] = None
    OrderExternalId: Optional[int] = None
    ProductTitle: Optional[str] = None
    FromOrderDate: Optional[datetime] = None
    ToOrderDate: Optional[datetime] = None
    ReservationStatus: Optional[List[int]] = None


@dataclass
class OrderLineReservationItemsExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None
