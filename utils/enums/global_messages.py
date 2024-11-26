from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = f"Received status code is not equal to expected"
    REQUIRED_FIELD_ERROR = "Not all fields are represented"
    WRONG_VALUE_EQUAL = "The value not equal expected value"
    WRONG_JSON_VALUE_IS_NOT_LESS = "The received value is not less than the expected value"
    WRONG_JSON_VALUE_IS_NOT_MORE = "The received value is not greater than the expected value"
    WRONG_CHECK_TOTAL_PRICE = "Total price is not corrected"
    WRONG_VARIABLE_CHECK = "The variable could not be checked"
    WRONG_PRODUCT_COUNT = "Product count not equal expected result"


class GlobalSuccessMessages(Enum):
    SUCCESSFUL_STATUS_CODE = "The received status code is valid"
    THERE_IS_NO_DISCOUNT = "The product has no discount"
