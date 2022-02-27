import sys
from main_page_local import MainPage

sys.path.append('../')


def test_admin_page(browser):
    """Проверка отображения главной страницы """
    page = MainPage(browser, 'http://localhost:8000/')
    page.open_main_page()
    a = page.admin_page().text
    page.admin_page().click()
    print(a)
    assert a in 'Go to Admin'


def test_regist_page(browser):
    """Вход в админику"""
    page = MainPage(browser, 'http://localhost:8000/')
    page.open_main_page()
    page.admin_page().click()
    welcome = page.regist_page()
    print(welcome)
    assert welcome in "WELCOME, ADMIN. VIEW SITE / CHANGE PASSWORD / LOG OUT"


def test_availability_group(browser, create_connection):
    """Проверка, что группа отображается созданная в базе данных"""
    cursor = create_connection
    cursor.execute("INSERT INTO auth_group(id, name) VALUES(5,'varf')")

    page = MainPage(browser, 'http://localhost:8000/')
    page.open_main_page()
    page.admin_page().click()
    page.regist_page()
    name = page.groups_page()
    print(name)
    assert name in 'varf'


if __name__ == '__main__':
    print("Let`s go!")
