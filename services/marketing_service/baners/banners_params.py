from dataclasses import dataclass
from typing import Optional


@dataclass
class DeleteBannerPlace:
    BannerPlaceId: Optional[int] = None


@dataclass
class BannerPlaces:
    BannerPlaceKind: Optional[int] = None


@dataclass
class BannerPlaceDetails:
    BannerPlaceId: Optional[int] = None


@dataclass
class RemoveBanner:
    BannerPlaceId: Optional[int] = None
    BannerId: Optional[int] = None


@dataclass
class DynamicBannerPlace:
    OwnerLink: Optional[str] = None


@dataclass
class Details:
    BannerPlaceId: Optional[int] = None


@dataclass
class DynamicBannerPlaces:
    OwnerLink: Optional[int] = None
