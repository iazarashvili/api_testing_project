from dataclasses import dataclass
from typing import Optional


@dataclass
class Features:
    searchValue: Optional[str] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    id: Optional[int] = None
