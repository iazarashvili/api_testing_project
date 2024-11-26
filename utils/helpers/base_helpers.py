import hashlib
from utils.enums import status_code, global_messages
from utils.enums.global_messages import GlobalErrorMessages, GlobalSuccessMessages
from utils.enums.status_code import StatusCode


class HelpFunctions:
    @staticmethod
    def create_md5(event_type: str, external_order_line_id: str, status: str):
        config_id = '45d6bf81-e8b7-4bfd-8158-508d41ea2f15'
        input_string = f'{event_type}{external_order_line_id}{status}{config_id}'
        md5 = hashlib.md5()
        md5.update(input_string.encode('ascii'))
        return md5.hexdigest().upper()

    @staticmethod
    def check_response_is_200(response):
        assert response.status_code == StatusCode.OK.value, \
            f'{global_messages.GlobalErrorMessages.WRONG_STATUS_CODE.value}. expect status is {response.status_code}'

    @staticmethod
    def check_response_is_500(response):
        assert response.status_code == StatusCode.internalServerError.value, \
            f'{GlobalErrorMessages.WRONG_STATUS_CODE.value}. expect status is {response.status_code}'

    @staticmethod
    def check_response_is_204(response):
        assert response.status_code == StatusCode.noContent.value, \
            f'{GlobalErrorMessages.WRONG_STATUS_CODE.value}. expect status is {response.status_code}'

    @staticmethod
    def check_json_data_value(data, expected_result):
        if data != expected_result:
            raise ValueError(f'value {data} not equal expected result: {expected_result}')
        else:
            return data


# Example usage:
# event_type = 'OrderStatusChange'
# external_order_line_id = '422139'
# status = 'OrderLineProcessing'
# config_id = '45d6bf81-e8b7-4bfd-8158-508d41ea2f15'

# hash_input = f"{event_type}{external_order_line_id}{status}{config_id}"
# md5_hash = create_md5(event_type, external_order_line_id, status)
# my_hash = HelpFunctions.create_md5('OrderItemStatusChange', '422142', 'OrderItemDelivered')
# print(my_hash)
