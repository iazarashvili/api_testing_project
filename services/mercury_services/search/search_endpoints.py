from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.mercury_endpoint}/search'


class SearchEndpoint:
    post_search_go_go = f'{base_url}/go-go'
    post_search_billie_jean = f'{base_url}/billie-jean'
    post_search_cool_cat = f'{base_url}/cool-cat'
    post_mamma_mia = f'{base_url}/mamma-mia'
    post_sunny = f'{base_url}/sunny'
