from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Item:
    id: Optional[int] = None
    sortIndex: Optional[int] = None


@dataclass
class FeatureSuggestedValuesParams:
    requestId: Optional[str]
    brandId: Optional[int] = None
    modelId: Optional[int] = None
    searchValue: Optional[str] = None
    id: Optional[int] = None
    categoryId: Optional[int] = None
    featureId: Optional[int] = None
    item: Optional[List[Item]] = None
    nextItem: Optional[List[item]] = None
