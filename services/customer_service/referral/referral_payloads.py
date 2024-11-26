from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Referral:
    promoCode: Optional[str] = None
    benefitType: Optional[int] = None
    value: Optional[int] = None
    maxReturnValue: Optional[int] = None
    referralBenefitThreshold: Optional[int] = None


@dataclass
class AddMilestone:
    referCount: Optional[int] = None
    balanceBenefit: Optional[int] = None
    level: Optional[int] = None


@dataclass
class UpdateMilestone:
    id: Optional[int] = None
    referCount: Optional[int] = None
    balanceBenefit: Optional[int] = None
    level: Optional[int] = None


@dataclass
class ReceiveMilestone:
    externalId: Optional[str] = None
