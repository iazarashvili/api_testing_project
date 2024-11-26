from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.catalog_endpoint}date/now/utc'


class DateEndpoints:
    get_date_now_utc = f'{base_url}'
    post_date_now_utc = f'{base_url}'
