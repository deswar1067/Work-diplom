from main.main_page_local import MainPage, Data, main_page


def create_group(create_connection):
    cursor = create_connection
    cursor.execute("INSERT INTO auth_group(id, name) VALUES(5,'voin')")

def test_user_two_page(browser):
    """Создаем нового пользователя и заходим под его профилем"""
    page = MainPage(browser, main_page)
    page.open_main_page()
    page.admin_page().click()
    page.regist_page()
    page.get_user_two()  # не забудь удалить пользователя
    page.log_out().click()
    page.login_it()
    user = page.user_page(Data.add_user_two, Data.password_us_two)
    print(user)
    assert user in 'WELCOME, DOBRI_DRUG. VIEW SITE / CHANGE PASSWORD / LOG OUT'


def test_user_to_search(create_connection):
    """Проверяем наличе user базе данных"""
    cursor = create_connection
    cursor.execute("SELECT username FROM auth_user")
    user_two = cursor.fetchall()
    print(user_two)
    assert Data.add_user_two in str(user_two)


if __name__ == '__main__':
    print('Let`sgo!')
