from dataclasses import dataclass
from typing import Optional


@dataclass
class Juridical:
    JuridicalId: Optional[str] = None


@dataclass
class List:
    PageSize: Optional[int] = None
    Page: Optional[int] = None
    SearchValue: Optional[str] = None
