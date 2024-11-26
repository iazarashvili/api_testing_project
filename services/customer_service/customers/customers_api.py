import allure
import requests
from services.customer_service.customers.customers_endpoints import CustomersEndpoints
from config.headers import Headers


class CustomersApi:
    def __init__(self):
        super().__init__()
        self._endpoints = CustomersEndpoints()
        self._headers = Headers()

    @allure.step('PUT Customers update physical')
    def put_update_physical(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_physical(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT Customers change email')
    def put_change_email(self, payload):
        response = requests.put(
            url=self._endpoints.put_change_email(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT Customers confirm email')
    def put_confirm_email(self, payload):
        response = requests.put(
            url=self._endpoints.put_confirm_email(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST Customers add phone number')
    def post_add_phone_number(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_phone_number(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST Customers change avatar')
    def post_change_avatar(self, avatar_file_path):
        response = requests.post(
            url=self._endpoints.post_change_avatar(),
            files=avatar_file_path,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT Customers id delete avatar')
    def put_id_delete_avatar(self, customer_id):
        response = requests.put(
            url=self._endpoints.put_id_delete_avatar(customer_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE Customers phone number delete id')
    def delete_phone_number_delete_id(self, customer_id):
        response = requests.delete(
            url=self._endpoints.delete_phone_number_delete_id(customer_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT Customers phone number change default id')
    def put_phone_number_change_default_id(self, customer_id):
        response = requests.put(
            url=self._endpoints.put_phone_number_change_default_id(customer_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST Customers phone number send verification')
    def post_phone_number_send_verification(self, payload):
        response = requests.post(
            url=self._endpoints.post_phone_number_send_verification(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST Customer legal create')
    def post_legal_create(self, payload):
        response = requests.post(
            url=self._endpoints.post_legal_create(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST Customer add manager')
    def post_add_manager(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_manager(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE remove manager id customer id')
    def delete_remove_manager_id_customer_id(self, manager_id, customer_id):
        response = requests.delete(
            url=self._endpoints.delete_remove_manager_id_customer_id(manager_id, customer_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST Customers add address')
    def post_add_address(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_address(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers update address')
    def put_update_address(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_address(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE customers remove address address id customer id')
    def delete_remove_address_address_id_customer_id(self, address_id, customer_id):
        response = requests.delete(
            url=self._endpoints.delete_remove_address_address_id_customer_id(address_id, customer_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers update legal')
    def put_update_legal(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_legal(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST customers add multiple address')
    def post_add_multiple_address(self):
        pass

    @allure.step('POST customers add size guide')
    def post_add_size_guide(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_size_guide(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE customers remove size guide category id customer id')
    def delete_remove_size_guide_category_id_customer_id(self, category_id, customer_id):
        response = requests.delete(
            url=self._endpoints.delete_remove_size_guide_category_id_customer_id(category_id, customer_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST customers change payment method')
    def post_change_payment_method(self, params, numbers_array):
        """
        :param params: merchantId: str
        """
        response = requests.post(
            url=self._endpoints.post_change_payment_method(),
            params=params,
            json=numbers_array,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST customers change shipping options')
    def post_change_shipping_options(self, payload):
        response = requests.post(
            url=self._endpoints.post_change_shipping_options(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST customers product view')
    def post_customer_product_view(self, payload):
        response = requests.post(
            url=self._endpoints.post_customer_product_view(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers is opted for ads')
    def put_is_opted_for_ads(self, payload):
        response = requests.put(
            url=self._endpoints.put_is_opted_for_ads(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST customers add shipping address')
    def post_add_shipping_address(self, payload):
        response = requests.post(
            url=self._endpoints.post_add_shipping_address(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE customers remove shipping address id')
    def delete_remove_shipping_address_id(self, shipping_address_id, params):
        response = requests.delete(
            url=self._endpoints.delete_remove_shipping_address_id(shipping_address_id),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers change default shipping address')
    def put_change_default_shipping_address(self, payload):
        response = requests.put(
            url=self._endpoints.put_change_default_shipping_address(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers edit shipping address ')
    def put_edit_shipping_address(self, payload):
        response = requests.put(
            url=self._endpoints.put_edit_shipping_address(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers change basic address')
    def put_change_basic_address(self, payload):
        response = requests.put(
            url=self._endpoints.put_change_basic_address(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST customers change dashboard status')
    def post_change_dashboard_status(self, payload):
        response = requests.post(
            url=self._endpoints.post_change_dashboard_status(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST customers change merchant hes user information')
    def post_change_merchant_hes_user_information(self, payload):
        response = requests.post(
            url=self._endpoints.post_change_merchant_hes_user_information(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE customers user id guarantee')
    def delete_user_id_guarantee(self, user_id):
        response = requests.delete(
            url=self._endpoints.delete_user_id_guarantee(user_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers guarantee')
    def put_guarantee(self, payload):
        response = requests.put(
            url=self._endpoints.put_guarantee(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers delivery time')
    def put_delivery_time(self, payload):
        """
        :param payload:  merchantId: str: deliveryTime: int
        """
        response = requests.put(
            url=self._endpoints.put_delivery_time(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers update representative relationships')
    def put_update_representative_relationships(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_representative_relationships(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers add representative to merchant')
    def put_add_representative_to_merchant(self, payload):
        response = requests.put(
            url=self._endpoints.put_add_representative_to_merchant(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('DELETE customers remove representative from merchant')
    def delete_remove_representative_from_merchant(self, payload):
        response = requests.delete(
            url=self._endpoints.delete_remove_representative_from_merchant(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers update representative relationships by entity type')
    def put_update_representative_relationships_by_entity_type(self, payload):
        response = requests.put(
            url=self._endpoints.put_update_representative_relationships_by_entity_type(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('PUT customers post pone verification')
    def put_post_pone_verification(self, payload):
        response = requests.put(
            url=self._endpoints.put_post_pone_verification(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST customers merchant working hours')
    def post_merchant_working_hours(self, payload):
        responsive = requests.post(
            url=self._endpoints.post_merchant_working_hours(),
            json=payload,
            headers=self._headers.cms_token
        )
        return responsive

    @allure.step('GET customers physical customers')
    def get_physical_customers(self, params):
        responsive = requests.get(
            url=self._endpoints.get_get_physical_customers(),
            params=params,
            headers=self._headers.cms_token
        )
        return responsive

    @allure.step('GET customers physical')
    def get_physical(self, params):
        responsive = requests.get(
            url=self._endpoints.get_physical(),
            params=params,
            headers=self._headers.cms_token
        )
        return responsive

    @allure.step('GET customers physical customer external id by user id')
    def get_physical_customer_external_id_by_user_id(self, params):
        response = requests.get(
            url=self._endpoints.get_physical_customer_external_id_by_user_id(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers legal customers')
    def get_legal_customers(self, params):
        response = requests.get(
            url=self._endpoints.get_legal_customers(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers legal user id')
    def get_legal_user_id(self, user_id: str):
        response = requests.get(
            url=self._endpoints.get_legal_user_id(user_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers contact phone exists phone number')
    def get_contact_phone_exists_phone_number(self, phone_number: str):
        response = requests.get(
            url=self._endpoints.get_contact_phone_exists_phone_number(phone_number),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers legal exists identity number')
    def get_legal_exists_identity_number(self, identity_number: str):
        response = requests.get(
            url=self._endpoints.get_legal_exists_identity_number(identity_number),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers legal exists external id')
    def get_legal_exists_external_id(self, external_id):
        response = requests.get(
            url=self._endpoints.get_legal_exists_external_id(external_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers size guide category id customer id')
    def get_size_guide_category_id_customer_id(self, category_id, customer_id):
        response = requests.get(
            url=self._endpoints.get_size_guide_category_id_customer_id(category_id, customer_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers getsize guides')
    def get_getsize_guides(self, params):
        response = requests.get(
            url=self._endpoints.get_getsize_guides(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST customers payment methods customer ids')
    def post_payment_methods_customer_ids(self, payload):
        response = requests.post(
            url=self._endpoints.post_payment_methods_customer_ids(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers product views')
    def get_customer_product_views(self, params):
        """
        :param params:  DarkStoreId: int
        """
        response = requests.get(
            url=self._endpoints.get_customer_product_views(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers is adult')
    def get_is_adult(self):
        response = requests.get(
            url=self._endpoints.get_is_adult(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers shipping address')
    def get_shipping_address(self, params):
        response = requests.get(
            url=self._endpoints.get_shipping_address(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers top merchants')
    def get_top_merchants(self, params):
        """
        :param params:  PageNumber: int: PageSize: int: SearchText: str: ReferrerType: int
        """
        response = requests.get(
            url=self._endpoints.get_top_merchants(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('POST customers get customer addresses')
    def post_get_customer_addresses(self, payload):
        """
        :param payload:  userIds: [str]
        """
        response = requests.post(
            url=self._endpoints.post_get_customer_addresses(),
            json=payload,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers merchant details customer id')
    def get_merchant_details_customer_id(self, customer_id):
        response = requests.get(
            url=self._endpoints.get_merchant_details_customer_id(customer_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers merchants for sync')
    def get_merchants_for_sync(self, params):
        """
        :param params: lastId: int
        """
        response = requests.get(
            url=self._endpoints.get_merchants_for_sync(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers legal external id')
    def get_legal_external_id(self, external_id):
        response = requests.get(
            url=self._endpoints.get_legal_external_id(external_id),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers representatives merchants data')
    def get_representatives_merchants_data(self):
        response = requests.get(
            url=self._endpoints.get_representatives_merchants_data(),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers retrieve merchants with dashboard')
    def get_retrieve_merchants_with_dashboard(self, params):
        response = requests.get(
            url=self._endpoints.get_retrieve_merchants_with_dashboard(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers identifier details')
    def get_identifier_details(self, identifier: str):
        response = requests.get(
            url=self._endpoints.get_identifier_details(identifier),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers identifier merchant contact details')
    def get_identifier_merchant_contact_details(self, identifier: str):
        response = requests.get(
            url=self._endpoints.get_identifier_merchant_contact_details(identifier),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers representatives')
    def get_representatives(self, params):
        """
        :param params:  PageNumber: int: PageSize: int: SearchValue: str
        """
        response = requests.get(
            url=self._endpoints.get_representatives(),
            params=params,
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers merchant exists merchant contact')
    def get_merchant_exists_merchant_contact(self, merchant_contact: str):
        response = requests.get(
            url=self._endpoints.get_merchant_exists_merchant_contact(merchant_contact),
            headers=self._headers.cms_token
        )
        return response

    @allure.step('GET customers merchant priorities')
    def get_merchant_priorities(self):
        response = requests.get(
            url=self._endpoints.get_merchant_priorities(),
            headers=self._headers.cms_token
        )
        return response
