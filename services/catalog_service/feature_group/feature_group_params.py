import uuid
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class FeatureGroupParams:
    searchValue: Optional[str] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    id: Optional[int] = None
    requestId = uuid.uuid4()
