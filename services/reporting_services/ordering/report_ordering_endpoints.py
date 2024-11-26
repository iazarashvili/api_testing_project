from utils.data.endpoints_data import Endpoints

base_url = f'{Endpoints.reporting_endpoint}/ordering'


class ReportOrderingEndpoints:

    @staticmethod
    def get_shipping_packages_excel():
        return f'{base_url}/shipping-packages/excel'

    @staticmethod
    def get_ordering_excel():
        return f'{base_url}/excel'

    @staticmethod
    def get_items_excel():
        return f'{base_url}/items/excel'

    @staticmethod
    def get_items_full_report_excel():
        return f'{base_url}/items-full-report/excel'

    @staticmethod
    def get_order_item_excel():
        return f'{base_url}/order/item/excel'

    @staticmethod
    def get_order_accounting_excel():
        return f'{base_url}/order/accounting/excel'

    @staticmethod
    def get_user_financial_excel():
        return f'{base_url}/user/financial/excel'

    @staticmethod
    def get_vouchers_excel():
        return f'{base_url}/vouchers/excel'
