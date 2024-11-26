from dataclasses import dataclass, field, asdict
from typing import Optional, List


@dataclass
class Merchant:
    merchantId: Optional[str] = None
    commercialTitle: Optional[str] = None
    priority: Optional[int] = None


@dataclass
class EmployeeProfilePost:
    correlationId: Optional[str] = None
    userId: Optional[str] = None
    email: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    orderBandwidth: Optional[int] = None
    workingDays: Optional[List[int]] = field(default_factory=list)
    merchants: Optional[List[Merchant]] = field(default_factory=list)


@dataclass
class EmployeeProfilePut:
    correlationId: Optional[str] = None
    id: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    orderBandwidth: Optional[int] = None
    workingDays: Optional[List[int]] = field(default_factory=list)
    merchants: Optional[List[Merchant]] = field(default_factory=list)


@dataclass
class Vacations:
    correlationId: Optional[str] = None
    id: Optional[int] = None
    vacationDateFrom: Optional[str] = None
    vacationDateTo: Optional[str] = None
