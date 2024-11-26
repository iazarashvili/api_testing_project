from dataclasses import dataclass
from typing import Optional


@dataclass
class PreviousItem:
    id: Optional[int] = None
    sortIndex: Optional[int] = None


@dataclass
class FeatureGroupPayload:
    correlationId: Optional[str] = None
    caption: Optional[str] = None
    id: Optional[int] = None
    previousItem: list[Optional[PreviousItem]] = None
    item: list[Optional[PreviousItem]] = None
