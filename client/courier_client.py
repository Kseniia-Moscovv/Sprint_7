from client.base_client import BaseClient


class CourierClient(BaseClient):
    COURIER_URL = BaseClient.BASE_URL + '/courier'

    def create_courier(self, courier):
        return self.post(self.COURIER_URL, courier.to_dict())

    def login_courier(self, courier_credentials):
        return self.post(f'{self.COURIER_URL}/login', courier_credentials.__dict__)

    def delete_courier(self, courier_id):
        return self.delete(f'{self.COURIER_URL}/{courier_id}')
