from ..main_page_local import MainPage, Data, main_page


def test_admin_page(browser):
    """Создадим пользователя и добавим его в группу"""
    page = MainPage(browser, main_page)
    page.open_main_page()
    page.admin_page().click()
    page.regist_page()
    page.get_user()
    print(page.user_data())
    assert Data.add_user in page.user_data()


def test_user_in_group(create_connection):
    """Прверим есть ли в базе данный пользователь в группе"""
    cursor = create_connection
    cursor.execute("SELECT id FROM auth_user  where username = 'dikii_belarus'")  #вытаскиваем из таблицы
                                                                        # auth-user столбца dikii_belarus его айдишник
    a = cursor.fetchall()
    # aa = [x[0] for x in a]
    # print(aa)
    cursor.execute("SELECT user_id FROM auth_user_groups")
    b = cursor.fetchall()
    # bb = [x[0] for x in b]
    # print(bb)
    assert str(a) in str(b)


if __name__ == '__main__':
    print('Let`s go!')


