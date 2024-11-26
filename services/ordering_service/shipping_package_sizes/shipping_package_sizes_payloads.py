from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class ShippingPackageSizesPost:
    correlationId: Optional[str] = None
    name: Optional[str] = None
    sortIndex: Optional[int] = None


@dataclass
class ShippingPackageSizesPut:
    correlationId: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    sortIndex: Optional[int] = None
