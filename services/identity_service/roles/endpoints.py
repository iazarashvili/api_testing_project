from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.identity_endpoint}/Roles'


class RolesEndpoints:

    @staticmethod
    def get_roles():
        return base_url

    @staticmethod
    def post_roles():
        return base_url

    @staticmethod
    def get_roles_name(name: str):
        return f'{base_url}/{name}'

    @staticmethod
    def delete_name(name: str):
        return f'{base_url}/{name}'

    @staticmethod
    def get_name_permission(name: str):
        return f'{base_url}/{name}/permission'

    @staticmethod
    def post_name_permission(name: str):
        return f'{base_url}/{name}/permission'

    @staticmethod
    def delete_name_permission(name: str):
        return f'{base_url}/{name}/permission'
