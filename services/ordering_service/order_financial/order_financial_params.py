from dataclasses import dataclass
from typing import Optional


@dataclass
class Details:
    SubOrderId: Optional[str] = None
