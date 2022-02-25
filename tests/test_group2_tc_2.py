import time

from WD.main_page_local import MainPage


def test_delete_post(browser):
    page = MainPage(browser, 'http://localhost:8000/')
    page.open_main_page()
    page.admin_page().click()
    page.regist_page()
    page.post_page().click()
    page.delete_post()
    time.sleep(5)
