from dataclasses import dataclass
from typing import Optional, List


@dataclass
class CreateBannerPlace:
    name: Optional[str] = None
    section: Optional[int] = None
    bannerPlaceType: Optional[int] = None
    bannerPlaceKind: Optional[int] = None
    ownerLink: Optional[str] = None


@dataclass
class AddBanner:
    bannerPlaceId: Optional[int] = None
    name: Optional[str] = None
    link: Optional[str] = None
    fileName: Optional[str] = None
    sortIndex: Optional[int] = None
    status: Optional[int] = None
    bannerDescription: Optional[str] = None
    labelDescription: Optional[str] = None
    ribbonColor: Optional[str] = None
    isHero: Optional[bool] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None


@dataclass
class ChangeBannerStatus:
    bannerPlaceId: Optional[int] = None
    bannerId: Optional[int] = None
    bannerStatus: Optional[int] = None


@dataclass
class PreviousItem:
    id: Optional[int] = None
    sortIndex: Optional[int] = None


@dataclass
class Item:
    item: Optional[List[PreviousItem]] = None


@dataclass
class UpdateBannerSortIndex:
    bannerPlaceId: Optional[int] = None
    previousItem: Optional[List[PreviousItem]] = None
    item: Optional[List[Item]] = None


@dataclass
class UpdateBanner:
    bannerPlaceId: Optional[int] = None
    bannerId: Optional[int] = None
    fileName: Optional[str] = None
    name: Optional[str] = None
    link: Optional[str] = None
    bannerDescription: Optional[str] = None
    labelDescription: Optional[str] = None
    ribbonColor: Optional[str] = None
    status: Optional[int] = None
    isHero: Optional[bool] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None


@dataclass
class ChangeBannerPlaceOwner:
    bannerPlaceId: Optional[int] = None
    ownerLink: Optional[str] = None
