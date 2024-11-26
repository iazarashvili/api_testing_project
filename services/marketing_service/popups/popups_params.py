from dataclasses import dataclass
from typing import Optional


@dataclass
class Popups:
    type: Optional[int] = None


@dataclass
class AdminPanel:
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    Name: Optional[str] = None
    Type: Optional[int] = None
    Form: Optional[int] = None
    Status: Optional[int] = None
    PopUpType: Optional[int] = None
