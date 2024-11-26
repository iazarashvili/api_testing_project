from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class ShippingPackagesPost:
    correlationId: Optional[str] = None
    locationId: Optional[int] = None
    shippingPackageSizeId: Optional[int] = None
    shippingOptionId: Optional[int] = None
    shippingTime: Optional[str] = None
    successPageShippingInfoText: Optional[str] = None
    limit: Optional[int] = None
    amount: Optional[int] = None


@dataclass
class ShippingPackagesPut:
    correlationId: Optional[str] = None
    id: Optional[int] = None
    locationId: Optional[int] = None
    shippingPackageSizeId: Optional[int] = None
    shippingOptionId: Optional[int] = None
    shippingTime: Optional[str] = None
    successPageShippingInfoText: Optional[str] = None
    limit: Optional[int] = None
    amount: Optional[int] = None


@dataclass
class ImportMultiple:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ChangeActivation:
    correlationId: Optional[str] = None
    id: Optional[int] = None
    isActive: Optional[bool] = None
