from dataclasses import dataclass
from typing import Optional


@dataclass
class MobileCategoriesParams:
    categoryId: Optional[int] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None