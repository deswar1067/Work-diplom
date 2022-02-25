import json

from WD.main_request_pet import *


def test_create_pet():
    """Создание питомцы"""
    response = new_pets("https://petstore.swagger.io/v2/pet")
    assert response.status_code == 200


def test_find_pets_id():
    """Поиск питомца"""
    response = find_pets_id("https://petstore.swagger.io/v2/pet/938")
    assert response.status_code == 200


def test_update_name_pet():
    """Обновление имени питомца"""
    response = update_name_pet("https://petstore.swagger.io/v2/pet/938", "swordfisha")
    assert response.status_code == 200


def test_search_name():
    """Поиск обновленного питомца"""
    response = update_name("https://petstore.swagger.io/v2/pet/938")
    name = json.loads(response.text)
    # print(name["name"])
    assert name["name"] in "swordfisha"


if __name__ == '__main__':
    print('Let`s go!')
