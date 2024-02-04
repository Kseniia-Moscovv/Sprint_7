import allure
import requests

from client.courier_client import CourierClient
from fixtures.courier import prepare_courier
from model.courier.courier_credentials import CourierCredentials
from utils.courier_generator import generate_courier_data


class TestLoginCourier:
    @allure.title('Courier login test')
    @allure.description('Courier login positive check')
    def test_login_courier(self, prepare_courier):
        payload = generate_courier_data()
        courier = prepare_courier(payload)

        (data, status_code) = CourierClient().login_courier(CourierCredentials(courier.login, courier.password))

        assert status_code == requests.codes['ok']
        assert data['id'] is not None

    @allure.title('Courier login without required fields test')
    @allure.description('Courier login without login field negative check')
    def test_login_courier_without_login(self, prepare_courier):
        payload = generate_courier_data()
        courier = prepare_courier(payload)
        (data, status_code) = CourierClient().login_courier(CourierCredentials('', courier.password))

        assert status_code == requests.codes['bad_request']
        assert data['message'] == 'Недостаточно данных для входа'

    @allure.title('Courier login with wrong required fields test')
    @allure.description('Courier login with wrong password field negative check')
    def test_login_courier_with_wrong_pass(self, prepare_courier):
        payload = generate_courier_data()
        courier = prepare_courier(payload)
        (data, status_code) = CourierClient().login_courier(CourierCredentials(courier.login, 'courier.password'))

        assert status_code == requests.codes['not_found']
        assert data['message'] == 'Учетная запись не найдена'

    @allure.title('Login non existent courier test')
    @allure.description('Login non existent courier negative check')
    def test_login_non_existent_courier(self):
        payload = CourierCredentials('kotik_kotik', 'mur_mur')
        (data, status_code) = CourierClient().login_courier(CourierCredentials(payload.login, payload.password))

        assert status_code == requests.codes['not_found']
        assert data['message'] == 'Учетная запись не найдена'
