from dataclasses import dataclass
from typing import Optional


@dataclass
class ManufacturerCountriesParams:
    searchValue: Optional[str] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
