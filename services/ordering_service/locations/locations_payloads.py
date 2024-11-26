from dataclasses import dataclass
from typing import Optional


@dataclass
class LocationsPost:
    correlationId: Optional[str] = None
    caption: Optional[str] = None
    sortIndex: Optional[int] = None
    deliveryDays: Optional[int] = None


@dataclass
class LocationsPut:
    correlationId: Optional[str] = None
    id: Optional[int] = None
    caption: Optional[str] = None
    deliveryDays: Optional[int] = None


@dataclass
class DeliveryDate:
    correlationId: Optional[str] = None
    id: Optional[int] = None
    deliveryDays: Optional[int] = None
