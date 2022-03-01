
from ..main_page_local import MainPage, main_page


def test_delete_post(browser):
    page = MainPage(browser, main_page)
    page.open_main_page()
    page.admin_page().click()
    page.regist_page()
    page.post_page().click()
    page.delete_post()
