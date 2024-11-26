from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Items:
    id: Optional[int] = None
    sortIndex: Optional[int] = None


@dataclass
class Features:
    correlationId: Optional[str] = None
    featureGroupId: Optional[int] = None
    caption: Optional[str] = None
    status: Optional[int] = None
    type: Optional[int] = None
    id: Optional[int] = None
    previousItem: list[Optional[Items]] = None
    items: List[Optional[Items]] = None
