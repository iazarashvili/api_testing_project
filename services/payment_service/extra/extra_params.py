from dataclasses import dataclass
from typing import Optional


@dataclass
class BalanceTransactions:
    UserId: Optional[str] = None
    PageNumber: Optional[int] = None
    PageSize: Optional[int] = None


@dataclass
class OrderPaymentDetails:
    OrderId: Optional[str] = None
    OrderBankOfInstallments: Optional[int] = None


@dataclass
class OrderRefundDetails:
    OrderId: Optional[str] = None
