from dataclasses import dataclass
from typing import Optional, List


@dataclass
class CreateStaticPage:
    name: Optional[str] = None
    status: Optional[int] = None
    url: Optional[str] = None
    sortIndex: Optional[int] = None
    description: Optional[str] = None
    staticPageGroupId: Optional[int] = None


@dataclass
class UpdateStaticPage:
    id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[int] = None
    url: Optional[str] = None
    sortIndex: Optional[int] = None
    description: Optional[str] = None
    staticPageGroupId: Optional[int] = None


@dataclass
class CreateStaticPageGroup:
    name: Optional[str] = None
    status: Optional[int] = None
    sortIndex: Optional[int] = None


@dataclass
class UpdateStaticPageGroup:
    id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[int] = None
    sortIndex: Optional[int] = None
