from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Popups:
    name: Optional[str] = None
    type: Optional[int] = None
    appearanceHour: Optional[str] = None
    appearanceSeconds: Optional[str] = None
    form: Optional[int] = None
    link: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    status: Optional[int] = None
    fileName: Optional[str] = None
    popUpType: Optional[int] = None


@dataclass
class PopupsId:
    name: Optional[str] = None
    type: Optional[int] = None
    appearanceHour: Optional[str] = None
    appearanceSeconds: Optional[str] = None
    form: Optional[int] = None
    link: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    status: Optional[int] = None
    fileName: Optional[str] = None


@dataclass
class SendEmail:
    popUpId: Optional[int] = None
    email: Optional[str] = None
