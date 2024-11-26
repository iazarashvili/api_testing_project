from utils.data.endpoints_data import Endpoints
import uuid

base_url = f'{Endpoints.catalog_endpoint}/express'


class ExpressEndpoints:
    post_express = f'{base_url}'
    get_express_darkstore = f'{base_url}/darkstore?requestId={uuid.uuid4()}'
