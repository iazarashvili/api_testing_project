from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TransactionDetailsExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None


@dataclass
class OrderPaymentDetailsExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None


@dataclass
class PaymentDetailsExcel:
    From: Optional[datetime] = None
    To: Optional[datetime] = None
