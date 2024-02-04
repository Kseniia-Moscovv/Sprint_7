import allure
import pytest
import requests

from client.order_client import OrderClient
from constants.order import OrderConstants
from model.order.order import Order


class TestCreateOrder:
    @pytest.mark.parametrize('order_data', OrderConstants.ORDER_LIST)
    @allure.title('Order creation test')
    @allure.description('Order creation positive parametrize check')
    def test_create_order(self, order_data):
        payload = Order(*order_data)
        (data, status_code) = OrderClient().create_order(payload)

        assert status_code == requests.codes['created']
        assert data['track'] is not None




