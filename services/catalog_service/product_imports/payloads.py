from dataclasses import dataclass
from typing import Optional


@dataclass
class ImportMultiple:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ProductStockAndPricesUpdateMultiple:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ProductAssetsImportMultiple:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ProductDetailsUpdateMultiple:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ProductShippingPackageSizesUpdateMultiple:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ProductKeywordsUpdateMultiple:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ImportVariations:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ImportDeleteProducts:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ProductBrandsAndModelsUpdateMultiple:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ProductHasBestPriceChangeMultiple:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ProductUpdateHasGiftMultiple:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class ProductAddBundles:
    ContentType: Optional[str] = None
    ContentDisposition: Optional[str] = None
    Headers: Optional[object] = None
    Length: Optional[int] = None
    Name: Optional[str] = None
    FileName: Optional[str] = None


@dataclass
class RsProductTitle:
    file: Optional[str] = None


@dataclass
class ProductExpirationDate:
    file: Optional[str] = None


@dataclass
class ProductSortIndex:
    file: Optional[str] = None


@dataclass
class ProductMerchant:
    file: Optional[str] = None
