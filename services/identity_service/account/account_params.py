from dataclasses import dataclass
from typing import Optional


@dataclass
class External:
    scheme: Optional[str] = None
    returnUrl: Optional[str] = None


@dataclass
class ImpersonateUser:
    userId: Optional[str] = None


@dataclass
class ExternalLoginCallBack:
    returnUrl: Optional[str] = None


@dataclass
class SignOut:
    returnUrl: Optional[str] = None
