from dataclasses import dataclass
from typing import Optional


@dataclass
class LocationsDelete:
    Id: Optional[int] = None
    correlationId: Optional[str] = None
    requestId: Optional[str] = None


@dataclass
class LocationsGet:
    SearchValue: Optional[str] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    Caption: Optional[str] = None


@dataclass
class LocationsId:
    Id: Optional[int] = None
