from dataclasses import dataclass
from typing import Optional, List


@dataclass
class CustomerBenefitsAdmin:
    searchValue: Optional[str] = None
    page: Optional[int] = None
    pageSize: Optional[int] = None
