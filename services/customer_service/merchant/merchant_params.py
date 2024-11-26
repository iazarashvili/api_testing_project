from dataclasses import dataclass
from typing import Optional


@dataclass
class TimeslotDetails:
    MerchantUserId: Optional[str] = None
    CategoryId: Optional[int] = None
