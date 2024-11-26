from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class AbandonedCartsExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None


@dataclass
class WishlistProductsExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None
