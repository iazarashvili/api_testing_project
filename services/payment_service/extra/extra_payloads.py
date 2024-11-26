from dataclasses import dataclass
from typing import Optional


@dataclass
class AddBalanceFromExtra:
    userId: Optional[str] = None
    amount: Optional[int] = None
    userExternalId: Optional[int] = None
    description: Optional[str] = None


@dataclass
class RemoveBalanceFromExtra:
    userId: Optional[str] = None
    amount: Optional[int] = None
    userExternalId: Optional[int] = None
    description: Optional[str] = None


@dataclass
class UseVoucher:
    userId: Optional[str] = None
    amount: Optional[int] = None
    voucherCode: Optional[str] = None
