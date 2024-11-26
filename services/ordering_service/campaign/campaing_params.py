from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Campaign:
    campaignId: Optional[int] = None
    DiscountType: Optional[List[int]] = None
    CampaignStatus: Optional[int] = None
    CampaignChannel: Optional[int] = None
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    SearchValue: Optional[str] = None
    CartTotalAmount: Optional[float] = None
    ReferrerType: Optional[int] = None
