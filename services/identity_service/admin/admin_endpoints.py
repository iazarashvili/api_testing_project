from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.identity_endpoint}/Admin'


class AdminEndpoints:

    @staticmethod
    def post_legal_update():
        return f'{base_url}/Legal/Update'

    @staticmethod
    def post_legal_reset_password():
        return f'{base_url}/Legal/ResetPassword'

    @staticmethod
    def post_user_create():
        return f'{base_url}/User/Create'

    @staticmethod
    def post_user_resend_temporary_password():
        return f'{base_url}/User/ResendTemporaryPassword'

    @staticmethod
    def put_user_role_update():
        return f'{base_url}/User/Role-Update'

    @staticmethod
    def delete_user_delete():
        return f'{base_url}/User/Delete'

    @staticmethod
    def get_user_employees():
        return f'{base_url}/User/Employees'

    @staticmethod
    def get_user_employees_for_profile():
        return f'{base_url}/user/employees-for-profile'

    @staticmethod
    def post_create_representative():
        return f'{base_url}/CreateRepresentative'

    @staticmethod
    def delete_remove_representative():
        return f'{base_url}/RemoveRepresentative'

    @staticmethod
    def post_user_authorize():
        return f'{base_url}/User/Authorize'

    @staticmethod
    def delete_by_admin():
        return f'{base_url}/delete/by-admin'

    @staticmethod
    def get_users_deleted():
        return f'{base_url}/Users/Deleted'
