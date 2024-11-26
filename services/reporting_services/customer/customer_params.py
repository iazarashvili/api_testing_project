from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class CustomerExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None


@dataclass
class KeywordsExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None
