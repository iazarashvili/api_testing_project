from dataclasses import dataclass
from typing import Optional


@dataclass
class AddCards:
    referrerType: Optional[int] = None
    bankType: Optional[int] = None
