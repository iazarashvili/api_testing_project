from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.identity_endpoint}/Profile'


class ProfileEndpoints:

    @staticmethod
    def post_email_send_verification():
        return f'{base_url}/email/sendverification'

    @staticmethod
    def phone_send_verification():
        return f'{base_url}/phone/sendverification'

    @staticmethod
    def post_change_user_name():
        return f'{base_url}/ChangeUserName'

    @staticmethod
    def post_change_phone():
        return f'{base_url}/ChangePhone'

    @staticmethod
    def post_change_password():
        return f'{base_url}/ChangePassword'

    @staticmethod
    def post_check_password():
        return f'{base_url}/CheckPassword'

    @staticmethod
    def post_send_reset_password_token():
        return f'{base_url}/SendResetPasswordToken'

    @staticmethod
    def post_reset_password():
        return f'{base_url}/ResetPassword'

    @staticmethod
    def post_delete():
        return f'{base_url}/delete'
