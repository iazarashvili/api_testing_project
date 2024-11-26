from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class ChangeReservationStatus:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderReservationItemId: Optional[int] = None
    reservationStatus: Optional[int] = None
    comment: Optional[str] = None
    addressId: Optional[int] = None


@dataclass
class OrderItemStatus:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    reservationOrderLineId: Optional[int] = None
    orderItemId: Optional[int] = None
    reservationOrderItemStatus: Optional[int] = None
    comment: Optional[str] = None
    addressId: Optional[int] = None


@dataclass
class ReservationOrderLineData:
    orderId: Optional[str] = None
    reservationOrderLineId: Optional[int] = None
    reservationStatus: Optional[int] = None


@dataclass
class OrderLineStatusMultiple:
    correlationId: Optional[str] = None
    reservationOrderLines: Optional[List[ReservationOrderLineData]] = field(default_factory=list)


# Пример данных


class OrderReservationPayloads:

    @staticmethod
    def put_change_order_reservation_status(order_gui_id, order_reservation_item_id, reservation_status):
        payload = {
            "orderId": order_gui_id,
            "orderReservationItemId": order_reservation_item_id,
            "reservationStatus": reservation_status
        }
        return payload
