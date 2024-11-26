from dataclasses import dataclass
from typing import Optional, List


@dataclass
class CreateSection:
    name: Optional[str] = None
    type: Optional[int] = None
    categoryId: Optional[int] = None
    categorySlug: Optional[str] = None
    setLink: Optional[str] = None
    webFileName: Optional[str] = None
    mobileFileName: Optional[str] = None
    webBannerPlaceId: Optional[int] = None
    mobileBannerPlaceId: Optional[int] = None
    sortIndex: Optional[int] = None


@dataclass
class ChangeSection:
    id: Optional[int] = None
    name: Optional[str] = None
    categoryId: Optional[int] = None
    categorySlug: Optional[str] = None
    setLink: Optional[str] = None
    webFileName: Optional[str] = None
    mobileFileName: Optional[str] = None
    webBannerPlaceId: Optional[int] = None
    mobileBannerPlaceId: Optional[int] = None


@dataclass
class SortIndex:
    id: Optional[int] = None
    sortIndex: Optional[int] = None
