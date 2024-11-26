from utils.enums.global_messages import GlobalErrorMessages


class BasketHelpers:

    @staticmethod
    def check_item_count(added_quantity, expected_value):
        if added_quantity != expected_value:
            raise TypeError(f'{GlobalErrorMessages.WRONG_VALUE_EQUAL.value}.'
                            f' Added value {added_quantity} expected value {expected_value}')

    @staticmethod
    def check_item_id(response, expected_value):
        if response.json()['data'][0]['productId'] != expected_value:
            raise TypeError(f'{GlobalErrorMessages.WRONG_VALUE_EQUAL.value}.'
                            f' Added value {expected_value} expected value {expected_value}')

    @staticmethod
    def check_total_price(response):
        total_price = []
        for item in response.data:
            total_price.append(item.price * item.productCount)
        if response.totalPrice != sum(total_price[0]):
            raise TypeError(f'Total price is not correct{total_price}, {response.totalPrice}')
        else:
            return total_price

    @staticmethod
    def check_value_not_equal_expected_value(data, expected_value):
        if data == expected_value:
            raise ValueError(f'Value {data} equal expected value {expected_value}')
        else:
            return data
