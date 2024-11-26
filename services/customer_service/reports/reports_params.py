from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Customers:
    From: Optional[str] = None
    To: Optional[str] = None
