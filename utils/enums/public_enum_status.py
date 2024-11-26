from enum import Enum


class PublicEnumStatus(Enum):
    OrderLineProcessing = 1
    CourierOrderItemPickedUp = 2
    WarehouseOrderExternalFailed = 3
    WarehouseOrderCanceledExternal = 4
    OrderLinePendingDelivery = 5
    CourierOrderPickedUp = 6
    OrderLineDeliveryInProgress = 7
    OrderLineDelivered = 8
    OrderLineCanceled = 9
    OrderItemProcessing = 10
    OrderItemPendingDelivery = 11
    OrderItemDeliveryInProgress = 12
    OrderItemDelivered = 13
    OrderItemCanceled = 14


class PublicEnumEventType(Enum):
    OrderStatusChange = 1
    OrderLineStatusChange = 2
    OrderItemStatusChange = 3
    InternalStatusChange = 4
