from dataclasses import asdict
from services.mercury_services.filters.filters_payloads import FiltersPayload


class FiltersData:

    @staticmethod
    def post_beat_it_data():
        data = FiltersPayload(
            categoryId=222,
            pageNumber=1,
            pageSize=48,
            brandIds=[],
            modelIds=[],
            sortType=1,
            sortBy=1,
            features={},
            merchantSlugs=[],
            darkStoreId=23,
            deliveryTypes=None
        )
        return asdict(data)
