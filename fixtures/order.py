import pytest

from client.courier_client import CourierClient
from client.order_client import OrderClient
from model.courier.courier_credentials import CourierCredentials
from utils.courier_generator import generate_courier_data
from utils.order_generator import generate_order_data


@pytest.fixture(scope='function')
def get_order_to_courier():
    courier = generate_courier_data()
    CourierClient().create_courier(courier)
    (courier_response, _) = CourierClient().login_courier(CourierCredentials(courier.login, courier.password))
    courier_id = courier_response['id']

    order = generate_order_data()
    (order_response, _) = OrderClient().create_order(order)
    order_track = order_response['track']

    (order_by_track_response, _) = OrderClient().get_order_id_by_track(order_track)
    order_id = order_by_track_response['order']['id']

    OrderClient().set_order_to_courier(order_id, courier_id)

    yield courier_id, order_track

    CourierClient().delete_courier(courier_id)
