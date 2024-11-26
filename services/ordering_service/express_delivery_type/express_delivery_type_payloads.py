from dataclasses import dataclass
from typing import Optional


@dataclass
class ExpressDeliveryType:
    correlationId: Optional[str] = None
