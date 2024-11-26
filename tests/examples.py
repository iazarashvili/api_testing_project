import json

import allure
import pytest
from dataclasses import asdict
from config.base_api import BaseApi
from utils.helper import Helper
import requests


@allure.epic('Basket epic')
class TestFirst(BaseApi, Helper):

    @allure.title('First test')
    def test_first(self):
        url = "https://customer.staging.extra.ge/api/upload/coverimage?requestId=1793190a-3310-93ea-4258-d6016ef64688"

        payload = {}
        files = [
            ('file', ('file', open('Screenshot_6.png', 'rb'), 'application/octet-stream'))
        ]
        headers = {
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjRBMEYxNkIzQjk0QkYzRUQxMDM2NjRENTk0RTYxMEJGOUJEMEQ2NURSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IlNnOFdzN2xMOC0wUU5tVFZsT1lRdjV2UTFsMCJ9.eyJuYmYiOjE3MTA5MTY1MzAsImV4cCI6MTc0MjQ1MjUzMCwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5zdGFnaW5nLmV4dHJhLmdlIiwiYXVkIjoiaWRlbnRpdHkiLCJjbGllbnRfaWQiOiJkZXYiLCJzdWIiOiJmNjMxYzEzNS02MTMxLTRkYTItODY1ZS02ZGM4ZWE5M2RhM2QiLCJhdXRoX3RpbWUiOjE3MTA5MTY1MzAsImlkcCI6ImxvY2FsIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiNzVkNDhjNzItNTEyNi00OWZiLWFjYmUtYWViMzBkMjBlNmJiIiwiVXNlckV4dGVybmFsSWQiOiIxODU3NjQiLCJlbWFpbCI6ImkuYXphcmFzaHZpbGlAYXJlYS5nZSIsImVtYWlsX3ZlcmlmaWVkIjoidHJ1ZSIsInBob25lX251bWJlciI6IjU4NDAwODU0NSIsInBob25lX251bWJlcl92ZXJpZmllZCI6ImZhbHNlIiwiTGFzdE5hbWUiOiLhg5Dhg5bhg5Dhg6Dhg5Dhg6jhg5Xhg5jhg5rhg5giLCJGaXJzdE5hbWUiOiLhg5jhg5rhg5jhg5AiLCJyb2xlIjoiQWRtaW4iLCJVc2VyVHlwZSI6IjEiLCJqdGkiOiI1Q0MxRkZBQTZGMTZBNDZFNDJDNkNCRTE1Qzg5OTg5QiIsImlhdCI6MTcxMDkxNjUzMCwic2NvcGUiOlsiYWRkcmVzcyIsImVtYWlsIiwiaWRlbnRpdHkiLCJvcGVuaWQiLCJwaG9uZSIsInByb2ZpbGUiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsicHdkIl19.jNXV_xea6RM3g_zDHk_1YdqGHvBZIn4OpVnw33jbN4SSRSLGKcZE2G3uu7GiMOrPUut-xXf2LpBfdqDE8YtkYMdCMfKYJosdLMF09BDx-WQZbmI-ZfeLQHblVqgD7h5DTaRJWkL2T0ajaFxBqmVEplhwh6alOmYiiujjsIrGwVG6KD6txZQ3hRoThVKZNiRvM9isGdjs2VFIlGXiKRtg_bcpBNvOS3YIivfbgpGywqDLKUqZSr_anlCHl0oEtJX4it9-KvMkV8BRQHhCSDjlnvOzsAJAJ3iXi1ikASNW6_rlOT-7jaWKrdUTA3FUJk1oRvJGK5wzjEnK6McC85QI8w',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://admin.staging.extra.ge/',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(response.json())

    def test_second(self):
        url = "https://customer.staging.extra.ge/api/customers/updatelegal?requestId=2df218ea-cfcf-7e41-f5e8-6ce8e99ec109"

        payload = json.dumps({
            "id": 209028,
            "identityNumber": "2390300000",
            "juridicalTitle": "test",
            "commercialTitle": "test",
            "commercialTitleEng": "test",
            "commercialTitleKa": "ტესტ",
            "agreementGuid": "5911556b-fea7-4050-887a-214b33b0f145.pdf",
            "externalId": None,
            "avatarGuid": "b5e7e515-fbcd-467c-bf59-366cae44ca34.jpg",
            "coverPhoto": "f6aa9fde-6b46-49a4-9a0f-b6e51e6f6c0e.jpg",
            "agreementUrl": "http://cdn.staging.extra.ge/docs/5911556b-fea7-4050-887a-214b33b0f145.pdf",
            "avatarUrl": "http://cdn.staging.extra.ge/images/avatars/b5e7e515-fbcd-467c-bf59-366cae44ca34.jpg",
            "coverPhotoUrl": None,
            "email": "vosew91632@cindalle.com",
            "phoneNumber": "501223344",
            "agreementType": 1,
            "contactPhoneNumber": "501223344",
            "priority": 1
        })
        headers = {
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjRBMEYxNkIzQjk0QkYzRUQxMDM2NjRENTk0RTYxMEJGOUJEMEQ2NURSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IlNnOFdzN2xMOC0wUU5tVFZsT1lRdjV2UTFsMCJ9.eyJuYmYiOjE3MTA5MTY1MzAsImV4cCI6MTc0MjQ1MjUzMCwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5zdGFnaW5nLmV4dHJhLmdlIiwiYXVkIjoiaWRlbnRpdHkiLCJjbGllbnRfaWQiOiJkZXYiLCJzdWIiOiJmNjMxYzEzNS02MTMxLTRkYTItODY1ZS02ZGM4ZWE5M2RhM2QiLCJhdXRoX3RpbWUiOjE3MTA5MTY1MzAsImlkcCI6ImxvY2FsIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiNzVkNDhjNzItNTEyNi00OWZiLWFjYmUtYWViMzBkMjBlNmJiIiwiVXNlckV4dGVybmFsSWQiOiIxODU3NjQiLCJlbWFpbCI6ImkuYXphcmFzaHZpbGlAYXJlYS5nZSIsImVtYWlsX3ZlcmlmaWVkIjoidHJ1ZSIsInBob25lX251bWJlciI6IjU4NDAwODU0NSIsInBob25lX251bWJlcl92ZXJpZmllZCI6ImZhbHNlIiwiTGFzdE5hbWUiOiLhg5Dhg5bhg5Dhg6Dhg5Dhg6jhg5Xhg5jhg5rhg5giLCJGaXJzdE5hbWUiOiLhg5jhg5rhg5jhg5AiLCJyb2xlIjoiQWRtaW4iLCJVc2VyVHlwZSI6IjEiLCJqdGkiOiI1Q0MxRkZBQTZGMTZBNDZFNDJDNkNCRTE1Qzg5OTg5QiIsImlhdCI6MTcxMDkxNjUzMCwic2NvcGUiOlsiYWRkcmVzcyIsImVtYWlsIiwiaWRlbnRpdHkiLCJvcGVuaWQiLCJwaG9uZSIsInByb2ZpbGUiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsicHdkIl19.jNXV_xea6RM3g_zDHk_1YdqGHvBZIn4OpVnw33jbN4SSRSLGKcZE2G3uu7GiMOrPUut-xXf2LpBfdqDE8YtkYMdCMfKYJosdLMF09BDx-WQZbmI-ZfeLQHblVqgD7h5DTaRJWkL2T0ajaFxBqmVEplhwh6alOmYiiujjsIrGwVG6KD6txZQ3hRoThVKZNiRvM9isGdjs2VFIlGXiKRtg_bcpBNvOS3YIivfbgpGywqDLKUqZSr_anlCHl0oEtJX4it9-KvMkV8BRQHhCSDjlnvOzsAJAJ3iXi1ikASNW6_rlOT-7jaWKrdUTA3FUJk1oRvJGK5wzjEnK6McC85QI8w',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://admin.staging.extra.ge/',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)
