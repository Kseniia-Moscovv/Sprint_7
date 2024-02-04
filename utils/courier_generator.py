import string
import random

from model.courier.courier import Courier
from utils.string_generator import generate_random_string


def generate_courier_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return Courier(login, password, first_name)
