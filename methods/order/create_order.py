"""Модуль содержит функцию по созданию заказа"""

import requests
import random
from faker import Faker
from methods.client.create_client import LAST_CLIENT

faker = Faker()
faker_ru = Faker('ru_RU')

BASE_URL = "http://service/v1/"
PHONE_CODE_LIST = [900, 901, 902, 903, 904, 905, 906, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917,
                   918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934,
                   936, 937, 938, 939, 941, 950, 951, 952, 953, 954, 955, 956, 958, 960, 961, 962, 963,
                   964, 965, 966, 967, 968, 969, 970, 971, 977, 978, 980, 981, 982, 983, 984, 985, 986,
                   987, 988, 989, 991, 992, 993, 994, 995, 996, 997, 999]


def create_order():
    """Функция создания заказа"""

    phone_code = random.choice(PHONE_CODE_LIST)
    phone_number = random.randint(1000000, 9999999)

    url_ending = "order/create"
    url = BASE_URL + url_ending

    data = {
        "client_id": LAST_CLIENT[-1],
        "address": faker.address().replace('\n', ' '),
        "phone": f"+7{phone_code}{phone_number}",
        "items": [
            {
              "item_id": random.randint(1, 9999999),
              "price": round(random.uniform(1, 9999), 2),
              "quantity": random.randint(1, 99),
            }
        ]
    }

    response = requests.request("POST", url, data=data)

    return response
