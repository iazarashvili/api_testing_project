from dataclasses import dataclass
from typing import Optional


class ModelParams:
    searchValue: Optional[str] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
