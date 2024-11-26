from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Vouchers:
    correlationId: Optional[str] = None
    price: Optional[int] = None
    fileName: Optional[str] = None
    type: Optional[int] = None
    recipientName: Optional[str] = None
    recipientPhone: Optional[str] = None
    recipientEmail: Optional[str] = None
    letterContent: Optional[str] = None
    vouchersCount: Optional[int] = None
    productId: Optional[int] = None


@dataclass
class Validate:
    VoucherCode: Optional[str] = None


@dataclass
class VoucherDetails:
    VoucherId: Optional[str] = None
