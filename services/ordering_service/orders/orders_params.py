from dataclasses import dataclass, asdict, astuple
from typing import Optional, List
import uuid


@dataclass
class Orders:
    PromoCode: Optional[str] = None
    userType: Optional[int] = None
    requestId: Optional[str] = None


@dataclass
class OrdersGet:
    SearchValue: Optional[str] = None
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    Status: Optional[List[int]] = None
    PersonalNumber: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PaymentType: Optional[List[int]] = None
    PriceFrom: Optional[float] = None
    PriceTo: Optional[float] = None
    CreateTimeFrom: Optional[str] = None
    CreateTimeTo: Optional[str] = None
    PromoCode: Optional[str] = None
    DeliveryType: Optional[List[int]] = None
    CampaignId: Optional[int] = None
    ReferrerType: Optional[int] = None
    ShippingOptionId: Optional[int] = None
    OrderId: Optional[int] = None
    OrderGeneralStatus: Optional[List[int]] = None
    OrderCancellationReason: Optional[List[int]] = None
    IsFirstOrder: Optional[bool] = None
    OwnerEmployee: Optional[str] = None
    CustomerType: Optional[List[int]] = None
    ContainsOutOfStockOrderItem: Optional[bool] = None


@dataclass
class CreateOrderByAdministrator:
    userId: Optional[str] = None
    PromoCode: Optional[str] = None
    UserType: Optional[int] = None
    requestId: Optional[str] = None


@dataclass
class OrderLineExternalFailedAction:
    ExternalFailedAction: Optional[int] = None
    OrderLineId: Optional[int] = None
    OrderId: Optional[int] = None
    ExtraComment: Optional[str] = None
    AddressId: Optional[int] = None
    Address: Optional[str] = None
    ReturnAddressId: Optional[int] = None
    City: Optional[str] = None
    CorrelationId: Optional[str] = None
    requestId: Optional[str] = None


@dataclass
class OrderItemExternalFailedAction:
    ExternalFailedAction: Optional[int] = None
    OrderLineId: Optional[int] = None
    OrderId: Optional[int] = None
    OrderItemId: Optional[int] = None
    ExtraComment: Optional[str] = None
    AddressId: Optional[int] = None
    City: Optional[str] = None
    Address: Optional[str] = None
    ReturnAddressId: Optional[int] = None
    CorrelationId: Optional[str] = None
    requestId: Optional[str] = None


@dataclass
class ForCustomerWeb:
    searchValue: Optional[str] = None
    page: Optional[int] = None
    pageSize: Optional[int] = None
    OrderFilterForCustomerType: Optional[int] = None


@dataclass
class GetOrderLineStatusChangeHistory:
    OrderId: Optional[str] = None
    ProductId: Optional[int] = None


@dataclass
class GetOrderProductsView:
    Page: Optional[int] = None
    PageSize: Optional[int] = None
    MerchantName: Optional[str] = None
    ProductTitle: Optional[str] = None
    OrderId: Optional[int] = None
    CreatedFrom: Optional[str] = None
    CreatedTo: Optional[str] = None
    OrderLineStatus: Optional[int] = None
    Reservist: Optional[str] = None
    OrderLineGeneralStatus: Optional[int] = None
    ShippingOptionId: Optional[int] = None
    OrderGeneralStatus: Optional[int] = None
    ReservationStatus: Optional[List[int]] = None
    DeliveryStatus: Optional[int] = None
    IsFirstOrder: Optional[bool] = None
    DeliveryDateFrom: Optional[str] = None
    DeliveryDateTo: Optional[str] = None
    SubOrderId: Optional[str] = None


@dataclass
class OrderInvoice:
    OrderExternalId: Optional[int] = None


class OrderParams:
    @staticmethod
    def post_order_params():
        data = Orders(userType=1, requestId=uuid.uuid4())
        return asdict(data)
