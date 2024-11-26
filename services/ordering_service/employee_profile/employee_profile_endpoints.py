import uuid

from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.ordering_endpoint}/employeeprofile'


class EmployeeProfileEndpoints:

    @staticmethod
    def post_employee_profile():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def put_employee_profile():
        return f'{base_url}?requestId={uuid.uuid4()}'

    @staticmethod
    def get_employee_profile():
        return base_url

    @staticmethod
    def patch_vacation():
        return f'{base_url}/vacation?requestId={uuid.uuid4()}'

    @staticmethod
    def delete_employee_profile_id(profile_id: int):
        return f'{base_url}/{profile_id}?requestId={uuid.uuid4()}'

    @staticmethod
    def get_employee_profile_id(profile_id: int):
        return f'{base_url}/{profile_id}'

    @staticmethod
    def get_info():
        return f'{base_url}/info'

    @staticmethod
    def get_info_user_user_id(user_id: str):
        return f'{base_url}/info/user/{user_id}'

    @staticmethod
    def get_orders():
        return f'{base_url}/orders'
