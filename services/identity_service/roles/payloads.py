from dataclasses import dataclass
from typing import Optional


@dataclass
class Roles:
    id: Optional[str] = None
    name: Optional[str] = None
    normalizedName: Optional[str] = None
    concurrencyStamp: Optional[str] = None
