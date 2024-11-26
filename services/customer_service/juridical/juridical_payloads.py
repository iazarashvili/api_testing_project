from dataclasses import dataclass
from typing import Optional


@dataclass
class Juridical:
    juridicalTitle: Optional[str] = None
    juridicalId: Optional[str] = None
