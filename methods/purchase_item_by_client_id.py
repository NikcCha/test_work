"""Модуль содержит функцию по созданию заказа"""

import requests
from faker import Faker

faker = Faker()
faker_ru = Faker('ru_RU')
BASE_URL = "http://service/v1/"


def purchase_item_by_client_id(client_id, item_id):
    """Функция создания заказа"""

    url_ending = "item/purchase/by-client"
    url = BASE_URL + url_ending

    data = {
        "client_id": client_id,
        "item_ids": [item_id]
    }
    response = requests.request("GET", url, data=data)

    return response
