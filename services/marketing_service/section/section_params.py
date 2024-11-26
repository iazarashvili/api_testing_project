from dataclasses import dataclass
from typing import Optional


@dataclass
class SectionsAdmin:
    Page: Optional[int] = None
    PageSize: Optional[int] = None


@dataclass
class SectionDetails:
    Id: Optional[int] = None


@dataclass
class Image:
    WebFileName: Optional[str] = None
    MobileFileName: Optional[str] = None
    SectionId: Optional[int] = None


@dataclass
class Section:
    SectionId: Optional[int] = None
