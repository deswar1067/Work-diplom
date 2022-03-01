import json
import time

from main.main_request_pet import *


def test_create_pet():
    """Создание питомцы"""
    response = new_pets("https://petstore.swagger.io/v2/pet")
    assert response.status_code == 200


def test_find_pets_id():
    """Поиск питомца"""
    # time.sleep(6)
    new_pets("https://petstore.swagger.io/v2/pet")
    response = find_pets_id("https://petstore.swagger.io/v2/pet/940")
    print(response.content)
    assert response.status_code == 200


def test_update_name_pet():
    """Обновление имени питомца"""
    time.sleep(6)

    update_name_pet("https://petstore.swagger.io/v2/pet/940", 'swordfish')
    response = update_name_pet("https://petstore.swagger.io/v2/pet/940", 'swordfish')
    assert response.status_code == 200


def test_search_name():
    """Поиск обновленного питомца"""
    # time.sleep(10)
    new_pets("https://petstore.swagger.io/v2/pet")
    response = update_name("https://petstore.swagger.io/v2/pet/940")
    name = json.loads(response.text)
    assert name["name"] in "swordfish"


def test_delete_pet():
    """Удаление питомца"""
    # time.sleep(6)
    new_pets("https://petstore.swagger.io/v2/pet")
    response = requests.delete("https://petstore.swagger.io/v2/pet/940")
    assert response.status_code == 200


if __name__ == '__main__':
    test_create_pet()
    test_find_pets_id()
    test_update_name_pet()
    test_search_name()
    test_delete_pet()

