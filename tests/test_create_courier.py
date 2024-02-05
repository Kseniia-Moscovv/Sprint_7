import allure
import requests
from client.courier_client import CourierClient
from model.courier.courier import Courier
from model.courier.courier_credentials import CourierCredentials
from utils.courier_generator import generate_courier_data


class TestCreateCourier:
    @allure.title('Courier creation test')
    @allure.description('Courier creation positive check')
    def test_create_courier(self, delete_courier):
        payload = generate_courier_data()
        (data, status_code) = CourierClient().create_courier(payload)

        assert status_code == requests.codes['created']
        assert data['ok'] == True

        delete_courier(CourierCredentials(payload.login, payload.password))

    @allure.title('Double courier creation test')
    @allure.description('Double courier creation negative check')
    def test_create_double_courier(self, delete_courier):
        payload = Courier('kotik_kotik', 'mur_mur_mur', 'Gershman')
        (_data, _status_code) = CourierClient().create_courier(payload)
        (data, status_code) = CourierClient().create_courier(payload)

        assert status_code == requests.codes['conflict']
        assert data['message'] == 'Этот логин уже используется'

        delete_courier(CourierCredentials(payload.login, payload.password))

    @allure.title('Courier creation without required fields test')
    @allure.description('Courier creation without password negative check')
    def test_create_courier_without_password(self):
        payload = Courier('kotik_kotik', '', 'Gershman')
        (data, status_code) = CourierClient().create_courier(payload)

        assert status_code == requests.codes['bad_request']
        assert data['message'] == 'Недостаточно данных для создания учетной записи'
