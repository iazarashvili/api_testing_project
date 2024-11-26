from dataclasses import dataclass
from typing import Optional


@dataclass
class UploadImage:
    File: Optional[str] = None
