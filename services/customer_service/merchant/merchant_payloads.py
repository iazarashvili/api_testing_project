from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TimeSlotOption:
    timeSlotOptionsId: Optional[int] = None
    slotType: Optional[int] = None


@dataclass
class Timeslot:
    merchantId: Optional[int] = None
    categoryId: Optional[int] = None
    merchantUserId: Optional[str] = None
    cutOffTimeType: Optional[int] = None
    merchantTimeSlotOptions: Optional[List[TimeSlotOption]] = None


@dataclass
class CutoffTime:
    merchantId: Optional[str] = None
    cutOffTime: Optional[int] = None
