from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateQr:
    orderId: Optional[str] = None


@dataclass
class StatusUpdate:
    orderId: Optional[str] = None
    status: Optional[int] = None
    description: Optional[str] = None
    secret: Optional[str] = None
