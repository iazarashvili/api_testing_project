import pytest
from config.base_api import BaseApi
from utils.data.data import Data


@pytest.fixture()
def empty_admin_basket():
    BaseApi.basket_admin_basket_api.post_empty_basket(Data.user_gui_id)


@pytest.fixture()
def empty_basket():
    BaseApi.basket_api.post_empty_basket()
