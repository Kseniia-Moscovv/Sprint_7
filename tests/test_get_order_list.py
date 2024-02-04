import allure
import requests

from client.order_client import OrderClient
from model.order.order import Order


class TestOrderList:
    @allure.title('Order list test')
    @allure.description('Get courier_s order list ')
    def test_get_order_list(self, get_order_to_courier):
        (courier_id, order_track) = get_order_to_courier

        (data, status_code) = OrderClient().get_order_list(courier_id)

        assert requests.codes['ok'] == status_code
        assert data['orders'][0]['track'] == order_track
        assert data['orders'][0]['courierId'] == courier_id
        assert data['pageInfo']['total'] == 1
