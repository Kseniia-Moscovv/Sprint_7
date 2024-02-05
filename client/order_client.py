from client.base_client import BaseClient
from constants.base import UrlConstants


class OrderClient(BaseClient):

    def create_order(self, order):
        return self.post(UrlConstants.ORDER_URL, order.to_dict())

    def get_order_list(self, courier_id):
        return self.get(UrlConstants.ORDER_URL, {'courierId': courier_id})

    def set_order_to_courier(self, order_track, courier_id):
        return self.put(f'{UrlConstants.ORDER_URL}/accept/{order_track}', {'courierId': courier_id})

    def get_order_id_by_track(self, order_track):
        return self.get(f'{UrlConstants.ORDER_URL}/track', {'t': order_track})
