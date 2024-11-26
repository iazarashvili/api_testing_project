from dataclasses import dataclass
from typing import Optional


@dataclass
class BalanceRefill:
    amount: Optional[int] = None
    returnUrl: Optional[str] = None


@dataclass
class Order:
    orderId: Optional[str] = None
    isCombinedPayment: Optional[bool] = None


@dataclass
class OrderReversal:
    orderId: Optional[str] = None
    amount: Optional[float] = None
    isBalanceRefundRequest: Optional[float] = None


@dataclass
class ShippingService:
    orderId: Optional[str] = None
    returnUrl: Optional[str] = None


@dataclass
class PremiumService:
    orderId: Optional[str] = None


@dataclass
class SponsorShip:
    id: Optional[int] = None


@dataclass
class OrderDept:
    id: Optional[int] = None
    paymentType: Optional[int] = None
    referrerType: Optional[int] = None
    cardId: Optional[int] = None


class PaymentPayloads:

    @staticmethod
    def post_payment(order_id):
        payload = {
            'orderId': order_id
        }
        return payload
