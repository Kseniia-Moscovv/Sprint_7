from client.base_client import BaseClient
from constants.base import UrlConstants


class CourierClient(BaseClient):

    def create_courier(self, courier):
        return self.post(UrlConstants.COURIER_URL, courier.to_dict())

    def login_courier(self, courier_credentials):
        return self.post(f'{UrlConstants.COURIER_URL}/login', courier_credentials.__dict__)

    def delete_courier(self, courier_id):
        return self.delete(f'{UrlConstants.COURIER_URL}/{courier_id}')
