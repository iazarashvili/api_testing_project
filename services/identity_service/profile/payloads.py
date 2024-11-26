from dataclasses import dataclass
from typing import Optional


@dataclass
class EmailSendVerification:
    email: Optional[str] = None


@dataclass
class PhoneSendVerification:
    phoneNumber: Optional[str] = None


@dataclass
class ChangeUserName:
    userName: Optional[str] = None
    otp: Optional[str] = None


@dataclass
class ChangePhone:
    phoneNumber: Optional[str] = None
    otp: Optional[str] = None


@dataclass
class ChangePassword:
    currentPassword: Optional[str] = None
    newPassword: Optional[str] = None


@dataclass
class CheckPassword:
    password: Optional[str] = None


@dataclass
class SendResetPasswordToken:
    jsonData: Optional[str] = None


@dataclass
class ResetPassword:
    token: Optional[str] = None
    password: Optional[str] = None
