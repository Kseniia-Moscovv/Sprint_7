import string
import random

from model.order.order import Order
from utils.string_generator import generate_random_string


def generate_order_data():
    first_name = generate_random_string(10)
    last_name = generate_random_string(10)
    address = generate_random_string(10)
    metro_station = str(random.randint(1, 10))
    phone = generate_random_string(11)
    rent_time = random.randint(1, 7)
    delivery_date = f'2024-{random.randint(1, 12)}-{random.randint(1, 28)}'
    comment = generate_random_string(10)
    color = []

    return Order(first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color)
