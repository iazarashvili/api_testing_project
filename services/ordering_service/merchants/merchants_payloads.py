from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Sales:
    merchantId: Optional[str] = None
    from_: Optional[str] = None
    to: Optional[str] = None
    categoryIds: Optional[List[int]] = field(default_factory=list)


@dataclass
class CategoryRanking:
    categoryIds: Optional[List[int]] = field(default_factory=list)
    merchantId: Optional[str] = None
