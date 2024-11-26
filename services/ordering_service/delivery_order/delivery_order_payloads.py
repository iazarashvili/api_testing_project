from dataclasses import dataclass
from typing import Optional


@dataclass
class DeliveryOrder:
    correlationId: Optional[str] = None
    deliveryOrderId: Optional[str] = None
    orderLineId: Optional[int] = None
    deliveryStatus: Optional[int] = None
