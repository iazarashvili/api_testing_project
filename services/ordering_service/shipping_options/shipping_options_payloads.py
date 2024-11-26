from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class ShippingOptionsPost:
    correlationId: Optional[str] = None
    type: Optional[int] = None
    caption: Optional[str] = None
    description: Optional[str] = None
    maxMerchantQuantity: Optional[int] = None


@dataclass
class ShippingOptionsPut:
    correlationId: Optional[str] = None
    id: Optional[int] = None
    caption: Optional[str] = None
    description: Optional[str] = None
    maxMerchantQuantity: Optional[int] = None
