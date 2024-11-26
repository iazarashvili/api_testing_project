from dataclasses import dataclass
from typing import Optional


@dataclass
class CheckStatus:
    orderId: Optional[str] = None
