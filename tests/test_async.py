import requests
import uuid

from config.headers import Headers


class TestReport:

    def test_report(self):
        response = requests.get(
            url=f'https://reporting.staging.extra.ge/api/ordering/excel?From=2024-06-02&To=2024-06-04&requestId={uuid.uuid4()}',
            headers=Headers.cms_token
        )
        with open('file.xls', 'wb') as f:
            f.write(response.content)
