from client.base_client import BaseClient


class OrderClient(BaseClient):
    ORDER_URL = BaseClient.BASE_URL + '/orders'

    def create_order(self, order):
        return self.post(self.ORDER_URL, order.to_dict())

    def get_order_list(self, courier_id):
        return self.get(self.ORDER_URL, {'courierId': courier_id})

    def set_order_to_courier(self, order_track, courier_id):
        return self.put(f'{self.ORDER_URL}/accept/{order_track}', {'courierId': courier_id})

    def get_order_id_by_track(self, order_track):
        return self.get(f'{self.ORDER_URL}/track', {'t': order_track})
