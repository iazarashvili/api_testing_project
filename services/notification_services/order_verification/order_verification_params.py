from dataclasses import dataclass
from typing import Optional


@dataclass
class Otp:
    orderId: Optional[str] = None
    otp: Optional[str] = None
