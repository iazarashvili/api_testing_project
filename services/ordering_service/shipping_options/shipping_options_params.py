from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class ShippingOptionsGet:
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
