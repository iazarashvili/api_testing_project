from dataclasses import dataclass
from typing import Optional


@dataclass
class Status:
    transactionId: Optional[str] = None


@dataclass
class StatusOrder:
    orderId: Optional[str] = None
