# class FiltersPayload:
#
#     @staticmethod
#     def post_filters_category_id():
#         payload = {
#             "categoryId": 3186,
#             "pageNumber": 1,
#             "pageSize": 48,
#             "brandIds": [],
#             "modelIds": [],
#             "sortType": 1,
#             "sortBy": 1,
#             "features": {},
#             "merchantSlugs": [],
#             "filterByDiscount": False,
#             "filterByGift": False,
#             "darkStoreId": 23,
#         }
#         return payload


from dataclasses import dataclass
from typing import Optional, List, Dict, Any


@dataclass
class FiltersPayload:
    categoryId: Optional[int] = None
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None
    brandIds: Optional[List[int]] = None
    modelIds: Optional[List[int]] = None
    sortType: Optional[int] = None
    sortBy: Optional[int] = None
    features: Optional[Dict[str, Any]] = None
    merchantSlugs: Optional[List[str]] = None
    darkStoreId: Optional[int] = None
    deliveryTypes: Optional[int] = None
