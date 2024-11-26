from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class FullExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class StockAndPricesExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class AssetsExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class DetailsExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class CategoriesExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class MerchantsExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class KeywordsExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class GuaranteesExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class GroupsExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class BrandsAndModelsExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class ProductHasPriceGuaranteeExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class ProductHasGiftExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class ContentReportExcel:
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None


@dataclass
class ProductBundlesExcel:
    request: Optional[object] = None


@dataclass
class ProductRsTitleExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class ProductExpirationDateExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class FirstPartyProductsExcel:
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class SponsoredProductsReportExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None


@dataclass
class SortIndexReportExcel:
    CategoryId: Optional[int] = None
    Status: Optional[int] = None
    UserId: Optional[str] = None
    SearchValue: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None


@dataclass
class CategoryTreeExcel:
    request: Optional[object] = None
