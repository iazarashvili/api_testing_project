from dataclasses import dataclass
from typing import Optional


class ModelPayloads:
    correlationId: Optional[str] = None
    brandId: Optional[int] = None
    categoryId: Optional[int] = None
    caption: Optional[str] = None
    status: Optional[int] = None
