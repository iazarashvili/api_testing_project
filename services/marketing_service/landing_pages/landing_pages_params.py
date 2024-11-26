from dataclasses import dataclass
from typing import Optional


@dataclass
class LandingPages:
    searchValue: Optional[str] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None


@dataclass
class LandingPagesId:
    id: Optional[int] = None


@dataclass
class LandingPagesIdProducts:
    searchValue: Optional[str] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
