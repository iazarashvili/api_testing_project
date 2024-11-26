from dataclasses import dataclass
from typing import Optional


@dataclass
class LegalUpdate:
    userId: Optional[str] = None
    email: Optional[str] = None
    phoneNumber: Optional[str] = None


@dataclass
class ResetPassword:
    userId: Optional[str] = None


@dataclass
class LegalUpdate:
    email: Optional[str] = None
    lastName: Optional[str] = None
    firstName: Optional[str] = None
    role: Optional[int] = None


@dataclass
class ResendTemporaryPassword:
    email: Optional[str] = None
    lastName: Optional[str] = None
    firstName: Optional[str] = None
    role: Optional[int] = None


@dataclass
class ResendTemporaryPassword:
    id: Optional[str] = None
    role: Optional[int] = None


@dataclass
class UserDelete:
    id: Optional[str] = None


@dataclass
class CreateRepresentative:
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    phoneNumber: Optional[str] = None


@dataclass
class RemoveRepresentative:
    userId: Optional[str] = None


@dataclass
class UserAuthorize:
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass
class DeleteByAdmin:
    userId: Optional[str] = None
