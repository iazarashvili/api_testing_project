from dataclasses import asdict
from services.mercury_services.search.search_payloads import Gogo, BillieJean, CoolCat, Sunny


class SearchData:
    @staticmethod
    def search_text(text: str):
        data = Gogo(
            searchText=text
        )
        return asdict(data)

    @staticmethod
    def search_billie_jane(search_text):
        data = BillieJean(
            brandIds=[],
            categoryId=None,
            darkStoreId=23,
            pageNumber=1,
            pageSize=48,
            searchText=search_text,
            sortBy=1,
            sortType=1
        )
        return asdict(data)

    @staticmethod
    def cool_cat(search_txt: str):
        data = CoolCat(
            searchText=search_txt
        )
        return asdict(data)

    @staticmethod
    def sunny():
        data = Sunny(
            categoryId=1,
            searchText='telefoni'
        )
        return asdict(data)
