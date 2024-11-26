from dataclasses import dataclass
from typing import Optional


@dataclass
class RemoveShippingAddressId:
    customerId: Optional[str] = None
    userType: Optional[int] = None


@dataclass
class GetPhysicalCustomers:
    searchValue: Optional[str] = None
    page: Optional[int] = None
    pageSize: Optional[int] = None


@dataclass
class Physical:
    UserId: Optional[str] = None


@dataclass
class GetPhysicalCustomerExternalIdByUserId:
    UserId: Optional[str] = None


@dataclass
class GetLegalCustomers:
    searchValue: Optional[str] = None
    page: Optional[int] = None
    pageSize: Optional[int] = None


@dataclass
class GetSizeGuide:
    customerId: Optional[str] = None
    page: Optional[int] = None
    pageSize: Optional[int] = None


@dataclass
class GetCustomerProductViews:
    DarkStoreId: Optional[int] = None


@dataclass
class GetShippingAddress:
    CustomerId: Optional[str] = None
    UserType: Optional[int] = None


@dataclass
class TopMerchants:
    PageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    SearchText: Optional[str] = None
    ReferrerType: Optional[int] = None


@dataclass
class GetMerchantsForSync:
    lastId: Optional[int] = None


@dataclass
class RetrieveMerchantsWithDashboard:
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    SearchValue: Optional[str] = None


@dataclass
class Representatives:
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None
    SearchValue: Optional[str] = None
