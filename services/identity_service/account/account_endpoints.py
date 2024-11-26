from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.identity_endpoint}/Account'


class AccountEndpoints:

    @staticmethod
    def get_external():
        return f'{base_url}/external'

    @staticmethod
    def get_impersonate_user():
        return f'{base_url}/ImpersonateUser'

    @staticmethod
    def get_is_impersonated_user():
        return f'{base_url}/IsImpersonatedUser'

    @staticmethod
    def get_external_login_call_back():
        return f'{base_url}/ExternalLoginCallBack'

    @staticmethod
    def get_sign_out():
        return f'{base_url}/SignOut'

    @staticmethod
    def get_exist_user_name(user_name: str):
        return f'{base_url}/exists/{user_name}'

    @staticmethod
    def post_register():
        return f'{base_url}/register'

    @staticmethod
    def post_send_verification():
        return f'{base_url}/sendverification'

    @staticmethod
    def post_send_password_reset_code():
        return f'{base_url}/sendpasswordresetcode'

    @staticmethod
    def post_verify():
        return f'{base_url}/verify'

    @staticmethod
    def post_set_password():
        return f'{base_url}/setpassword'

    @staticmethod
    def post_reset_password():
        return f'{base_url}/resetpassword'
