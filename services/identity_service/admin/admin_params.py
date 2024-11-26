from dataclasses import dataclass
from typing import Optional


@dataclass
class Employees:
    RoleName: Optional[str] = None
    FullName: Optional[str] = None
    Email: Optional[str] = None
    PageSize: Optional[int] = None
    PageNumber: Optional[int] = None


@dataclass
class UsersDeleted:
    PageSize: Optional[int] = None
    PageNumber: Optional[int] = None
    SearchValue: Optional[str] = None
