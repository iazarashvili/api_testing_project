from dataclasses import dataclass, field, asdict
from typing import List, Optional


@dataclass
class TimeSlotOption:
    startHour: Optional[str] = None
    endHour: Optional[str] = None
    before: Optional[int] = None
    after: Optional[int] = None


@dataclass
class TimeslotsPost:
    correlationId: Optional[str] = None
    slotType: Optional[int] = None
    shippingPrice: Optional[int] = None
    timeSlotOptions: List[TimeSlotOption] = field(default_factory=list)


@dataclass
class TimeSlotOption:
    id: Optional[int] = None
    startHour: Optional[str] = None
    endHour: Optional[str] = None
    before: Optional[int] = None
    after: Optional[int] = None


@dataclass
class TimeslotsPut:
    correlationId: Optional[str] = None
    id: Optional[int] = None
    shippingPrice: Optional[int] = None
    timeSlotOptions: List[TimeSlotOption] = field(default_factory=list)
