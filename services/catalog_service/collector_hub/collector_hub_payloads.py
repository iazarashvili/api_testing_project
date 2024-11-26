from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class ProductFeatureValue:
    featureId: Optional[int] = None
    featureValue: Optional[str] = None


@dataclass
class ProductAsset:
    extraProductId: Optional[int] = None
    fileName: Optional[str] = None
    type: Optional[int] = None
    sortIndex: Optional[int] = None
    url: Optional[str] = None


@dataclass
class Product:
    id: Optional[int] = None
    extraProductId: Optional[int] = None
    categoryId: Optional[int] = None
    userId: Optional[str] = None
    sku: Optional[str] = None
    mpn: Optional[str] = None
    brandId: Optional[int] = None
    modelId: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    sellPrice: Optional[int] = None
    price: Optional[int] = None
    discountedPrice: Optional[int] = None
    discountPercent: Optional[int] = None
    discountPeriodStartTime: Optional[datetime] = None
    discountPeriodEndTime: Optional[datetime] = None
    extraCommissionFeePercent: Optional[int] = None
    variationIdentifier: Optional[str] = None
    externalId: Optional[str] = None
    externalType: Optional[int] = None
    quantity: Optional[int] = None
    createdBy: Optional[str] = None
    discountTakePrice: Optional[int] = None
    discountExtraCommissionFeePercent: Optional[int] = None
    discountExtraCommissionFeeAmount: Optional[int] = None
    reSync: Optional[bool] = None
    darkStoreId: Optional[int] = None
    productFeatureValues: Optional[List[ProductFeatureValue]] = None
    productAssets: Optional[List[ProductAsset]] = None


@dataclass
class CollectorHubPayloads:
    correlationId: Optional[str] = None
    products: Optional[List[Product]] = None
