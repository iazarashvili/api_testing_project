from dataclasses import dataclass
from typing import Optional


@dataclass
class PostNamePermission:
    permission: Optional[str] = None


@dataclass
class DeleteNamePermission:
    permission: Optional[str] = None
