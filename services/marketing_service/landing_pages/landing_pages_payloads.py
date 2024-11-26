from dataclasses import dataclass
from typing import Optional, List


@dataclass
class LandingPagesPost:
    title: Optional[str] = None
    status: Optional[int] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None


@dataclass
class LandingPagesPut:
    id: Optional[int] = None
    title: Optional[int] = None
    status: Optional[int] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None


@dataclass
class LandingPagesDelete:
    id: Optional[int] = None


@dataclass
class ProductsAdd:
    productIds: Optional[list] = None


@dataclass
class ProductsRemove:
    productIds: Optional[list] = None
