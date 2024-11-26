from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.customer_endpoint}'


class CustomersEndpoints:

    @staticmethod
    def put_update_physical():
        return f'{base_url}/updatephysical'

    @staticmethod
    def put_change_email():
        return f'{base_url}/changeemail'

    @staticmethod
    def put_confirm_email():
        return f'{base_url}/confirmemail'

    @staticmethod
    def post_add_phone_number():
        return f'{base_url}/addphonenumber'

    @staticmethod
    def post_change_avatar():
        return f'{base_url}/changeavatar'

    @staticmethod
    def put_id_delete_avatar(customer_id):
        return f'{base_url}/{customer_id}/deleteavatar'

    # todo: გასარვევია რომელი აიდი უნდა გაიგზავნოს
    @staticmethod
    def delete_phone_number_delete_id(customer_id):
        return f'{base_url}/phonenumber/delete/{customer_id}'

    @staticmethod
    def put_phone_number_change_default_id(customer_id):
        return f'{base_url}/phonenumber/change-default/{customer_id}'

    @staticmethod
    def post_phone_number_send_verification():
        return f'{base_url}/phonenumber/sendverification'

    @staticmethod
    def post_legal_create():
        return f'{base_url}/legal/create'

    @staticmethod
    def post_add_manager():
        return f'{base_url}/addmanager'

    @staticmethod
    def delete_remove_manager_id_customer_id(manager_id, customer_id):
        return f'{base_url}/removemanager/{manager_id}/{customer_id}'

    @staticmethod
    def post_add_address():
        return f'{base_url}/addaddress'

    @staticmethod
    def put_update_address():
        return f'{base_url}/updateaddress'

    @staticmethod
    def delete_remove_address_address_id_customer_id(address_id, customer_id):
        return f'{base_url}/removeaddress/{address_id}/{customer_id}'

    @staticmethod
    def put_update_legal():
        return f'{base_url}/updatelegal'

    @staticmethod
    def post_add_multiple_address():
        return f'{base_url}/addmultipleaddress'

    @staticmethod
    def post_add_size_guide():
        return f'{base_url}/addsizeguide'

    @staticmethod
    def delete_remove_size_guide_category_id_customer_id(category_id, customer_id):
        return f'{base_url}/removesize'

    @staticmethod
    def post_change_payment_method():
        return f'{base_url}/changepaymentmethod'

    @staticmethod
    def post_change_shipping_options():
        return f'{base_url}/changeshippingoptions'

    @staticmethod
    def post_customer_product_view():
        return f'{base_url}/customer-product-view'

    @staticmethod
    def put_is_opted_for_ads():
        return f'{base_url}/is-opted-ads'

    @staticmethod
    def post_add_shipping_address():
        return f'{base_url}/add-shipping-address'

    @staticmethod
    def delete_remove_shipping_address_id(shipping_address_id):
        return f'{base_url}/remove-shipping-address/{shipping_address_id}'

    @staticmethod
    def put_change_default_shipping_address():
        return f'{base_url}/change-default-shippig-address'

    @staticmethod
    def put_edit_shipping_address():
        return f'{base_url}/edit-shipping-address'

    @staticmethod
    def put_change_basic_address():
        return f'{base_url}/change-basic-address'

    @staticmethod
    def post_change_dashboard_status():
        return f'{base_url}/change-dashboard-status'

    @staticmethod
    def post_change_merchant_hes_user_information():
        return f'{base_url}/change-merchant-hasuserinformation'

    @staticmethod
    def delete_user_id_guarantee(user_id):
        return f'{base_url}/{user_id}/guarantee'

    @staticmethod
    def put_guarantee():
        return f'{base_url}/guarantee'

    @staticmethod
    def put_delivery_time():
        return f'{base_url}/deliverytime'

    @staticmethod
    def put_update_representative_relationships():
        return f'{base_url}/updaterepresentativerelationships'

    @staticmethod
    def put_add_representative_to_merchant():
        return f'{base_url}/addrepresentativetomerchant'

    @staticmethod
    def delete_remove_representative_from_merchant():
        return f'{base_url}/removerepresentativefrommerchant'

    @staticmethod
    def put_update_representative_relationships_by_entity_type():
        return f'{base_url}/updaterepresentativerelationshipsbyentitytype'

    @staticmethod
    def put_post_pone_verification():
        return f'{base_url}/postponeverification'

    @staticmethod
    def post_merchant_working_hours():
        return f'{base_url}/merchant/workinghours'

    @staticmethod
    def get_get_physical_customers():
        return f'{base_url}/getphysicalcustomers'

    @staticmethod
    def get_physical():
        return f'{base_url}/physical'

    @staticmethod
    def get_physical_customer_external_id_by_user_id():
        return f'{base_url}getphysicalcustomerexternalidbyuserid'

    @staticmethod
    def get_legal_customers():
        return f'{base_url}/getlegalcustomers'

    @staticmethod
    def get_legal_user_id(user_id):
        return f'{base_url}/legal/{user_id}'

    @staticmethod
    def get_contact_phone_exists_phone_number(phone_number):
        return f'{base_url}/contact-phone/exists/{phone_number}'

    @staticmethod
    def get_legal_exists_identity_number(identity_number):
        return f'{base_url}/legal/exists/{identity_number}'

    @staticmethod
    def get_legal_exists_external_id(external_id):
        return f'{base_url}/legal/exists/external/{external_id}'

    @staticmethod
    def get_size_guide_category_id_customer_id(category_id, customer_id):
        return f'{base_url}/sizeguide/{category_id}/{customer_id}'

    @staticmethod
    def get_getsize_guides():
        return f'{base_url}/getsizeguides'

    @staticmethod
    def post_payment_methods_customer_ids():
        return f'{base_url}/paymentmethods/customerids'

    @staticmethod
    def get_customer_product_views():
        return f'{base_url}/get-customer-product-views'

    @staticmethod
    def get_is_adult():
        return f'{base_url}/is-adult'

    @staticmethod
    def get_shipping_address():
        return f'{base_url}/get-shipping-address'

    @staticmethod
    def get_top_merchants():
        return f'{base_url}/top-merchants'

    @staticmethod
    def post_get_customer_addresses():
        return f'{base_url}/getcustomeradresses'

    @staticmethod
    def get_merchant_details_customer_id(customer_id):
        return f'{base_url}/merchant-details/{customer_id}'

    @staticmethod
    def get_merchants_for_sync():
        return f'{base_url}/getmerchantsforsync'

    @staticmethod
    def get_legal_external_id(external_id):
        return f'{base_url}/external/{external_id}'

    @staticmethod
    def get_representatives_merchants_data():
        return f'{base_url}/representatives/merchants-data'

    @staticmethod
    def get_retrieve_merchants_with_dashboard():
        return f'{base_url}/retrievemerchantswithdashboard'

    @staticmethod
    def get_identifier_details(identifier):
        return f'{base_url}/{identifier}/details'

    @staticmethod
    def get_identifier_merchant_contact_details(identifier):
        return f'{base_url}/{identifier}/merchant-contact-details'

    @staticmethod
    def get_representatives():
        return f'{base_url}/representatives'

    @staticmethod
    def get_merchant_exists_merchant_contact(merchant_contact):
        return f'{base_url}/merchant/exists/{merchant_contact}'

    @staticmethod
    def get_merchant_priorities():
        return f'{base_url}/merchant/priorities'
