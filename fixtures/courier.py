import pytest

from client.courier_client import CourierClient
from model.courier.courier_credentials import CourierCredentials


@pytest.fixture(scope='function')
def prepare_courier():
    courier = {}

    def _prepare_courier(data):
        nonlocal courier
        CourierClient().create_courier(data)
        courier = data
        return courier

    yield _prepare_courier

    (login_response, _) = CourierClient().login_courier(CourierCredentials(courier.login, courier.password))
    CourierClient().delete_courier(login_response['id'])


@pytest.fixture(scope='function')
def delete_courier():
    def _delete_courier(data):
        (login_response, _) = CourierClient().login_courier(data)
        CourierClient().delete_courier(login_response['id'])

    return _delete_courier
