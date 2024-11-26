from utils.data.data import Data


class Headers:
    web_token = {
        'accept': 'application/json, text/plain, */*',
        "Authorization": f"Bearer {Data.web_token}",
        'origin': 'https://staging.extra.ge',
        'Content-Type': 'application/json'
    }

    cms_token = {
        'accept': 'application/json, text/plain, */*',
        "Authorization": f"Bearer {Data.cms_token}",
        'origin': 'https://admin.staging.extra.ge',
    }

    izi_box_token = {
        'accept': 'application/json, text/plain, */*',
        "Authorization": f"Bearer {Data.izi_box_token}",
    }

    not_authorize = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/json-patch+json',
        'dnt': '1',
        'origin': 'https://basket.staging.extra.ge',
        'pragma': 'no-cache',
        'referer': 'https://basket.staging.extra.ge/swagger/index.html',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
    }
