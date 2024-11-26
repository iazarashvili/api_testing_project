from dataclasses import dataclass
from typing import Optional


@dataclass
class RemoveStaticPage:
    Id: Optional[int] = None
    Status: Optional[int] = None


@dataclass
class RemoveStaticPage:
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    Name: Optional[str] = None
    Status: Optional[int] = None
    Description: Optional[str] = None
    SortIndex: Optional[int] = None
    Url: Optional[str] = None
    StaticPageGroupId: Optional[int] = None


@dataclass
class StaticPageDetails:
    Id: Optional[int] = None


@dataclass
class RemoveStaticPageGroup:
    Id: Optional[int] = None


@dataclass
class StaticPageGroups:
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    Name: Optional[str] = None
    Status: Optional[int] = None
    SortIndex: Optional[int] = None


@dataclass
class GetStaticPageGroupsForDropDown:
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    Name: Optional[str] = None


@dataclass
class StaticPageGroupDetails:
    StaticPageGroupId: Optional[int] = None


@dataclass
class StaticPageDescription:
    url: Optional[str] = None
