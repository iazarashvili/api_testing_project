from dataclasses import dataclass
from typing import Optional


@dataclass
class CardsGet:
    bankType: Optional[int] = None


@dataclass
class CardsPost:
    bankType: Optional[int] = None


@dataclass
class GetByCardType:
    type: Optional[int] = None
    bankType: Optional[int] = None
