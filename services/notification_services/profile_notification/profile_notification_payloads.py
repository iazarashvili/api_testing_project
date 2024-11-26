from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ProfileNotification:
    userId: Optional[str] = None
    description: Optional[str] = None
    type: Optional[int] = None
    orderUserId: Optional[str] = None
    orderId: Optional[str] = None
    orderExternalId: Optional[int] = None
    orderLineId: Optional[int] = None
    orderItemId: Optional[int] = None


@dataclass
class ProfileNotificationIdStatus:
    status: Optional[int]
   