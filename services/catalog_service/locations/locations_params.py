from dataclasses import dataclass
from typing import Optional


@dataclass
class LocationParams:
    searchValue: Optional[str] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
