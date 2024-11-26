from dataclasses import dataclass
from typing import Optional


@dataclass
class Verify:
    orderId: Optional[str] = None
    otp: Optional[str] = None
