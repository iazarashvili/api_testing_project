from dataclasses import dataclass
from typing import Optional


@dataclass
class Payment:
    payment_hash: Optional[str] = None
    status: Optional[str] = None
    order_id: Optional[str] = None
    ipay_payment_id: Optional[str] = None
    status_description: Optional[str] = None
    shop_order_id: Optional[str] = None
    transaction_id: Optional[str] = None
    pan: Optional[str] = None
    payment_method: Optional[str] = None
    multi_merchant_transaction_id: Optional[str] = None


@dataclass
class Reversal:
    payment_hash: Optional[str] = None
    status: Optional[str] = None
    order_id: Optional[str] = None
    ipay_payment_id: Optional[str] = None
    status_description: Optional[str] = None
    shop_order_id: Optional[str] = None
    transaction_id: Optional[str] = None
    payment_method: Optional[str] = None
