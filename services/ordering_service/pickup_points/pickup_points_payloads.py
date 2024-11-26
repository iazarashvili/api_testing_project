from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class PickupPointsPost:
    correlationId: Optional[str] = None
    shippingOptionId: Optional[int] = None
    locationId: Optional[int] = None
    addressDisplayName: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    workingHours: Optional[str] = None
    phoneNumber: Optional[str] = None


@dataclass
class PickupPointsPut:
    correlationId: Optional[str] = None
    id: Optional[int] = None
    addressDisplayName: Optional[str] = None
    phoneNumber: Optional[str] = None
    workingHours: Optional[str] = None
