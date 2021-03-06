from main.main_request_user import *


def test_create_user():
    """Создание пользователя"""
    response = create_user("https://petstore.swagger.io/v2/user")
    assert response.status_code == 200


def test_login_user():
    """Регистрация пользователя"""
    response = register_user("https://petstore.swagger.io/v2/user/login?username=deswar1067&password=123", 'deswar1067',
                             "123")
    print(response)
    assert response.status_code == 200


def test_find_user():
    """Поиск пользователя"""
    response = get_data_user("https://petstore.swagger.io/v2/user/deswar1067", 'deswar1067')
    assert response.status_code == 200


def test_logout():
    """Выход пользователя из системы"""
    response = logout("https://petstore.swagger.io/v2/user/logout")
    assert response.status_code == 200


def test_delete():
    """Удаление пользователя"""
    response = delete_user("https://petstore.swagger.io/v2/user/deswar1067")
    assert response.status_code == 200


if __name__ == '__main__':
    test_create_user()
    test_login_user()
    test_find_user()
    test_logout()
    test_delete()
