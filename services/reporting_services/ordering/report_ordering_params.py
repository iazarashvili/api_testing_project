from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class ShippingPackagesExcel:
    LocationId: Optional[int] = None
    ShippingPackageSizeId: Optional[int] = None
    Limit: Optional[float] = None
    Amount: Optional[float] = None


@dataclass
class OrderingExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None
    Status: Optional[int] = None


@dataclass
class ItemsExcel:
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    MerchantName: Optional[str] = None
    ProductTitle: Optional[str] = None
    CreatedFrom: Optional[str] = None
    CreatedTo: Optional[datetime] = None
    OrderId: Optional[int] = None
    OrderLineStatus: Optional[int] = None
    SKU: Optional[str] = None
    Reservist: Optional[str] = None
    OrderLineGeneralStatus: Optional[int] = None
    ReservationStatus: Optional[int] = None


@dataclass
class ItemsFullReportExcel:
    MerchantName: Optional[str] = None
    CreatedFrom: Optional[str] = None
    CreatedTo: Optional[datetime] = None
    ShippingOptionId: Optional[int] = None
    ReservationStatus: Optional[int] = None


@dataclass
class OrderItemsExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None


@dataclass
class OrderAccountingExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None


@dataclass
class UserFinancialExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None


@dataclass
class VouchersExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None
