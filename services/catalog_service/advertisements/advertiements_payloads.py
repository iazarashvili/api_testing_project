from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class AdvertisementsPayload:
    correlationId: Optional[str] = None
    customerId: Optional[str] = None
    brandId: Optional[int] = None
    status: Optional[int] = None
    imageFileName: Optional[str] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    url: Optional[str] = None
    id: Optional[int] = None
    advertisementId: Optional[int] = None
    categories: Optional[list] = None

    @staticmethod
    def delete_advertisements(correlation_id, any_id):
        payload = AdvertisementsPayload(
            correlationId=correlation_id,
            id=any_id
        )
        return asdict(payload)

    @staticmethod
    def post_update_categories(correlation_id, advertisement_id, categories):
        payload = AdvertisementsPayload(
            correlationId=correlation_id,
            advertisementId=advertisement_id,
            categories=categories
        )
        return asdict(payload)
