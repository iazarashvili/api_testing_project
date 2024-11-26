from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class ShippingPackageSizesDelete:
    Id: Optional[int] = None
    CorrelationId: Optional[str] = None
    requestId: Optional[str] = None


@dataclass
class ShippingPackageSizesId:
    Id: Optional[int] = None
