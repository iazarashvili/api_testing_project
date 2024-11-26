from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class AdvertisementsParams:
    pageNumber: Optional[int] = None
    pageSize: Optional[int] = None

    @staticmethod
    def first_params(page_number, page_size):
        params = AdvertisementsParams(
            pageNumber=page_number,
            pageSize=page_size
        )
        return asdict(params)
