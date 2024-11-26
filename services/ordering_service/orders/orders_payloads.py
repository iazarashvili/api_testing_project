from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict
import uuid


@dataclass
class PhoneNumber:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    phoneNumber: Optional[str] = None


@dataclass
class UpdateOrder:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    personalNumber: Optional[str] = None
    phoneNumber: Optional[str] = None
    location: Optional[str] = None
    address: Optional[str] = None
    addressAdditionalInfo: Optional[str] = None
    longitude: Optional[int] = None
    latitude: Optional[int] = None


@dataclass
class ChangeOrderCancelReason:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    reason: Optional[int] = None


@dataclass
class ProductAdd:
    productId: Optional[str] = None
    productCount: Optional[str] = None


@dataclass
class ImageUrls:
    large: Optional[str] = None
    medium: Optional[str] = None
    small: Optional[str] = None


@dataclass
class OrderLine:
    productId: Optional[int] = None
    productCount: Optional[int] = None
    shippingOptionId: Optional[int] = None
    expressDeliveryTypeId: Optional[int] = None
    districtId: Optional[int] = None
    expressType: Optional[int] = None
    timeSlotOptionsId: Optional[int] = None
    deliveryDate: Optional[str] = None
    imageUrls: Optional[ImageUrls] = None


@dataclass
class CreateOrderByAdministrator:
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    phoneNumber: Optional[str] = None
    personalNumber: Optional[str] = None
    locationId: Optional[int] = None
    location: Optional[str] = None
    address: Optional[str] = None
    addressAdditionalInfo: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    paymentType: Optional[int] = None
    bankOfInstalments: Optional[int] = None
    additionalInformation: Optional[str] = None
    referrerType: Optional[int] = None
    paymentFlowType: Optional[int] = None
    orderLines: Optional[List[OrderLine]] = field(default_factory=list)
    installmentType: Optional[str] = None
    installmentMonths: Optional[int] = None
    shouldSaveCard: Optional[bool] = None
    cardId: Optional[int] = None
    isRememberCard: Optional[bool] = None
    comment: Optional[str] = None
    shippingOptionId: Optional[int] = None
    darkStoreId: Optional[int] = None
    districtId: Optional[int] = None
    voucherType: Optional[int] = None
    voucherIds: Optional[List[str]] = field(default_factory=list)
    pickupPointId: Optional[int] = None
    isCombinedPayment: Optional[bool] = None


@dataclass
class ChangeOrderExtraCash:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    extraCash: Optional[int] = None
    shippingPrice: Optional[int] = None


@dataclass
class OrderDeliveryTypeChange:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    deliveryType: Optional[int] = None


@dataclass
class ChangeOrderBankOfInstalments:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    bankOfInstalments: Optional[int] = None


@dataclass
class ChangeMerchantAddressForOrder:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderLineId: Optional[int] = None
    productAddressId: Optional[int] = None
    city: Optional[str] = None
    address: Optional[str] = None


@dataclass
class ChangeOrderPaymentType:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderPaymentType: Optional[int] = None


@dataclass
class ChangeOrderDeliveryMethod:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    deliveryType: Optional[int] = None


@dataclass
class ChangeOrderComment:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    additionalInformation: Optional[str] = None


@dataclass
class ChangeOrderLineComment:
    orderId: Optional[str] = None
    productId: Optional[int] = None
    comment: Optional[str] = None
    correlationId: Optional[str] = None


@dataclass
class ChangeOrderGeneralStatus:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderGeneralStatus: Optional[int] = None
    orderCancellationReason: Optional[int] = None
    reason: Optional[str] = None


@dataclass
class OrderLineGeneralStatus:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderLineId: Optional[int] = None
    orderLineGeneralStatus: Optional[int] = None


@dataclass
class ChangeMerchantWillPickup:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderLineId: Optional[int] = None
    merchantWillPickUp: Optional[bool] = None


@dataclass
class OwnerEmployee:
    correlationId: Optional[str] = None
    orderIds: Optional[List[str]] = field(default_factory=list)
    ownerEmployee: Optional[str] = None


@dataclass
class OrderItemMerchantWillPickup:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderLineId: Optional[int] = None
    orderItemId: Optional[int] = None
    merchantWillPickUp: Optional[bool] = None


@dataclass
class OrderLinesOrderItemPost:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderLineId: Optional[int] = None
    darkStoreId: Optional[int] = None
    itemCount: Optional[int] = None


@dataclass
class OrderLinesOrderItemDelete:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderLineId: Optional[int] = None
    orderItemId: Optional[int] = None
    darkStoreId: Optional[int] = None
    itemCount: Optional[int] = None


@dataclass
class OrderItemGeneralStatus:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderLineId: Optional[int] = None
    orderItemId: Optional[int] = None
    orderItemGeneralStatus: Optional[int] = None


@dataclass
class MerchantAddressOrderItem:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderLineId: Optional[int] = None
    orderItemId: Optional[int] = None
    addressId: Optional[int] = None
    city: Optional[str] = None
    address: Optional[str] = None


@dataclass
class OrderItemComment:
    orderId: Optional[str] = None
    orderItemId: Optional[int] = None
    orderLineId: Optional[int] = None
    comment: Optional[str] = None
    correlationId: Optional[str] = None


@dataclass
class GeneralStatusForAdmin:
    correlationId: Optional[str] = None
    orderExternalId: Optional[int] = None
    orderGeneralStatus: Optional[int] = None


@dataclass
class ChangeOrderStatusMultiple:
    correlationId: Optional[str] = None
    orderIds: Optional[List[str]] = None
    orderGeneralStatus: Optional[int] = None
    orderCancellationReason: Optional[int] = None


@dataclass
class OrderLineDeliveryDate:
    correlationId: Optional[str] = None
    orderId: Optional[str] = None
    orderLineId: Optional[int] = None
    deliveryDate: Optional[str] = None
    timeSlotOptionsId: Optional[int] = None


@dataclass
class Merchant:
    categoryId: Optional[int] = None
    merchantId: Optional[str] = None


@dataclass
class CheckValidTimeslot:
    correlationId: Optional[str] = None
    locationId: Optional[int] = None
    merchants: Optional[List[Merchant]] = field(default_factory=list)
    productTimeSlotOptionIds: Optional[List[int]] = field(default_factory=list)


@dataclass
class OrderChangeHistories:
    orderId: Optional[str] = None
    searchValue: Optional[int] = None
    orderChangeHistoryTypes: Optional[List[int]] = None
    page: Optional[int] = None
    pageSize: Optional[int] = None


@dataclass
class Item:
    productId: Optional[int] = None
    price: Optional[float] = None
    title: Optional[str] = None
    imageUrl: Optional[str] = None
    installmentPrice: Optional[float] = None
    productCount: Optional[int] = None
    discountedPrice: Optional[float] = None
    discountedPercent: Optional[float] = None
    quantity: Optional[int] = None
    isPreOrderProduct: Optional[bool] = None
    commercialTitle: Optional[str] = None
    customerId: Optional[str] = None
    discountType: Optional[int] = None
    discountValue: Optional[float] = None
    valueType: Optional[int] = None
    productSlug: Optional[str] = None
    sellerSlug: Optional[str] = None
    sellerId: Optional[int] = None
    productDiscountPrice: Optional[float] = None
    deliveryDate: Optional[str] = None
    shippingOptionId: Optional[int] = None
    isExpress: Optional[bool] = None
    isActiveProduct: Optional[bool] = None
    sku: Optional[str] = None
    timeSlotOptionsId: Optional[int] = None
    timeSlotOptions: Optional[str] = None
    categoryId: Optional[int] = None
    shippingPackageSizeId: Optional[int] = None
    voucherId: Optional[str] = None


@dataclass
class CheckoutPrices:
    paymentType: Optional[int] = None
    location: Optional[int] = None
    items: Optional[List[Item]] = field(default_factory=list)
    bankOfInstalments: Optional[int] = None
    userId: Optional[str] = None
    promoCode: Optional[str] = None
    referrerType: Optional[int] = None
    cardId: Optional[int] = None
    shippingOptionId: Optional[int] = None
    darkStoreId: Optional[int] = None
    districtId: Optional[int] = None
    expressType: Optional[int] = None
    userType: Optional[int] = None
    isGroupOrder: Optional[bool] = None
    shippingOptionType: Optional[int] = None


@dataclass
class SuccessPageShippingInfoText:
    orderId: Optional[str] = None


class OrdersPayload:

    @staticmethod
    def order_payload(order_lines):
        payload = {
            "firstName": "Python",
            "lastName": "Tests",
            "phoneNumber": "595300019",
            "personalNumber": "342432443424",
            "locationId": 1,
            "location": "თბილისი",
            "comment": None,
            "bankOfInstalments": None,
            "referrerType": 0,
            "paymentFlowType": 0,
            "paymentType": 8,
            "additionalInformation": None,
            "orderLines":
                order_lines,
            "installmentType": None,
            "installmentMonths": None,
            "shippingOptionId": None,
            "id": 1491,
            "address": "17 ვახტანგ ჩიქოვანის ქუჩა, თბილისი, საქართველო",
            "addressAdditionalInfo": None,
            "longitude": 44.7522063,
            "latitude": 41.7308501,
            "isDefault": True,
            "darkStoreId": 23,
            "districtId": 12
        }
        return payload

    # item_json ში უნდა გადაეცეს ბასკეტიდან დაბრუნებული ჯეისონი აითემის
    @staticmethod
    def post_checkout_prices_payload(items_json, product_total_price):
        payload = {
            "paymentType": 8,
            "bankOfInstalments": None,
            "location": 1,
            "items": items_json,
            "isRememberCard": False,
            "districtId": 12,
            "darkStoreId": 23,
            "isGroupOrder": True,
            "productTotalPrice": product_total_price,
            "removeInactiveProducts": True,
            "userType": 1,
            "type": "[BASKET] GetCheckOutBasket"
        }
        return payload
