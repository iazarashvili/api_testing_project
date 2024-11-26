from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ProfileNotification:
    SearchQuery: Optional[str] = None
    Statuses: List[Optional[int]] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
