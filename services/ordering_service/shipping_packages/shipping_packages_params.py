from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class ShippingPackagesDelete:
    Id: Optional[int] = None
    correlationId: Optional[str] = None
    requestId: Optional[str] = None


@dataclass
class ShippingPackagesGet:
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    LocationId: Optional[int] = None
    ShippingPackageSizeId: Optional[int] = None
    ShippingOptionId: Optional[int] = None
    Limit: Optional[float] = None
    Amount: Optional[float] = None
