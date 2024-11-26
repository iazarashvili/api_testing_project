from dataclasses import dataclass
from typing import Optional


@dataclass
class RegisterDevice:
    token: Optional[str] = None
    tokenHolderType: Optional[int] = None


@dataclass
class UnregisterDevice:
    token: Optional[str] = None


@dataclass
class ChangeRegistrationToken:
    deviceId: Optional[str] = None
    oldToken: Optional[str] = None
    newToken: Optional[str] = None


@dataclass
class ValidateToken:
    registrationToken: Optional[str] = None


@dataclass
class RegisterApnToken:
    apnsToken: Optional[str] = None
    subOrderId: Optional[str] = None
