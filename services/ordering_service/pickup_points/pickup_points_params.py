from dataclasses import dataclass, asdict
from typing import Optional, List


@dataclass
class PickupPointsDelete:
    Id: Optional[int] = None
    CorrelationId: Optional[str] = None
    requestId: Optional[str] = None


@dataclass
class PickupPointsGet:
    ShippingOptionId: Optional[int] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None


@dataclass
class LocationsCheckout:
    ProductIds: Optional[List[int]] = None
