from dataclasses import dataclass
from typing import Optional


@dataclass
class FeatureSuggestedValuesPayloads:
    correlationId: Optional[str] = None
    categoryId: Optional[int] = None
    featureId: Optional[int] = None
    brandId: Optional[int] = None
    modelId: Optional[int] = None
    value: Optional[str] = None
    status: Optional[int] = None
    id: Optional[int] = None

