from dataclasses import dataclass
from typing import Optional


@dataclass
class IpayCheckStatus:
    iPayInstallmentId: Optional[int] = None


@dataclass
class TbcCheckStatus:
    orderId: Optional[int] = None
