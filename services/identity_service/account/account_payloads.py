from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class External:
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    emailOrPhone: Optional[str] = None
    birthDate: Optional[datetime] = None


@dataclass
class SendVerification:
    username: Optional[str] = None


@dataclass
class SendPasswordResetCode:
    username: Optional[str] = None


@dataclass
class Verify:
    username: Optional[str] = None
    otp: Optional[str] = None


@dataclass
class SetPassword:
    username: Optional[str] = None
    password: Optional[str] = None
    token: Optional[str] = None


@dataclass
class ResetPassword:
    username: Optional[str] = None
    otp: Optional[str] = None
