from dataclasses import dataclass
from typing import Optional


@dataclass
class Status:
    correlationId: Optional[str] = None
    id: Optional[str] = None
