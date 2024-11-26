from dataclasses import dataclass
from typing import Optional


@dataclass
class Installments:
    orderId: Optional[str] = None
