import requests
import allure

from services.ordering_service.employee_profile.employee_profile_endpoints import EmployeeProfileEndpoints
from config.headers import Headers


class EmployeeProfileApi:
    def __init__(self):
        super().__init__()
        self._endpoints = EmployeeProfileEndpoints()
        self._headers = Headers()

    def post_employee_profile(self, payload):
        response = requests.post(
            url=self._endpoints.post_employee_profile(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def put_employee_profile(self, payload):
        response = requests.put(
            url=self._endpoints.put_employee_profile(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def get_employee_profile(self, params):
        response = requests.get(
            url=self._endpoints.get_employee_profile(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    def patch_vacation(self, payload):
        response = requests.patch(
            url=self._endpoints.patch_vacation(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    def delete_employee_profile_id(self, profile_id: int):
        response = requests.delete(
            url=self._endpoints.delete_employee_profile_id(profile_id),
            headers=self._headers.cms_token
        )
        return response

    def get_employee_profile_id(self, profile_id: int):
        response = requests.get(
            url=self._endpoints.get_employee_profile_id(profile_id),
            headers=self._headers.cms_token
        )
        return response

    def get_employee_profile_info(self):
        response = requests.get(
            url=self._endpoints.get_info(),
            headers=self._headers.cms_token
        )
        return response

    def get_info_user_user_id(self, user_id: str):
        response = requests.get(
            url=self._endpoints.get_info_user_user_id(user_id),
            headers=self._headers.cms_token
        )
        return response

    def get_employee_profile_orders(self, params):
        response = requests.get(
            url=self._endpoints.get_orders(),
            params=params,
            headers=self._headers.cms_token
        )
        return response
