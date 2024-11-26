from dataclasses import dataclass
from typing import Optional


@dataclass
class HasActiveOrder:
    AddressId: Optional[int] = None
    MerchantId: Optional[str] = None
