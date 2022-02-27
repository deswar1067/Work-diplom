from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .base_page import BasePage


class Locator_GR1:
    locator_admin = (By.CSS_SELECTOR, "body > main > section > div > p:nth-child(3) > a")
    locator_user = (By.NAME, "username")
    locator_password = (By.NAME, "password")
    locator_submit = (By.XPATH, '//*[@id="login-form"]/div[3]/input')
    locator_welcome = (By.ID, 'user-tools')
    locator_groups = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[1]/th/a')
    locator_groups_name = (By.CSS_SELECTOR, '#result_list > tbody > tr > th > a')
    locator_add_user = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[2]/td[1]/a')
    locator_continue = (By.NAME, '_continue')
    locator_username = (By.NAME, 'username')
    locator_userpass = (By.NAME, 'password1')
    locator_userpass_confirm = (By.NAME, 'password2')
    locator_id_staff = (By.ID, 'id_is_staff')
    locator_id_superuser = (By.ID, 'id_is_superuser')
    # locator_search_group = (By.CSS_SELECTOR, '#id_groups_from > option') '''для добавления пользователя в группу
    # осуществляем поиск по названию
    locator_user_add_group = (By.ID, "id_groups_add_all_link")
    locator_save = (By.NAME, "_save")
    locator_user_data = (By.CLASS_NAME, 'field-username')


class Locator_GR2:
    locator_log_out = (By.CSS_SELECTOR, '#user-tools > a:nth-child(4)')


class Data:
    user = 'admin'
    password = 'password'
    add_user = 'dikii_belarus'
    password_us = 'orsha1992'
    add_user_two = 'dobri_drug'
    password_us_two = 'dobrota123'


class MainPage(BasePage):

    def login_it(self):
        self.find_element((By.CSS_SELECTOR, '#content > p:nth-child(3) > a')).click()

    def user_page(self, user='', password=''):
        self.find_element(Locator_GR1.locator_user).send_keys(user)
        self.find_element(Locator_GR1.locator_password).send_keys(password)
        self.find_element(Locator_GR1.locator_submit).click()
        welcome = self.find_element(Locator_GR1.locator_welcome).text
        return welcome

    def admin_page(self):
        search_home = self.find_element(Locator_GR1.locator_admin)
        return search_home

    def regist_page(self):
        self.find_element(Locator_GR1.locator_user).send_keys(Data.user)
        self.find_element(Locator_GR1.locator_password).send_keys(Data.password)
        self.find_element(Locator_GR1.locator_submit).click()
        welcome = self.find_element(Locator_GR1.locator_welcome).text
        return welcome

    def groups_page(self):
        self.find_element(Locator_GR1.locator_groups).click()
        name = self.find_element(Locator_GR1.locator_groups_name).text
        return name

    def get_user(self):
        self.find_element(Locator_GR1.locator_add_user).click()
        self.find_element(Locator_GR1.locator_username).send_keys(Data.add_user)
        self.find_element(Locator_GR1.locator_userpass).send_keys(Data.password_us)
        self.find_element(Locator_GR1.locator_userpass_confirm).send_keys(Data.password_us)
        self.find_element(Locator_GR1.locator_continue).click()
        self.find_element(Locator_GR1.locator_id_staff).click()
        self.find_element(Locator_GR1.locator_id_superuser).click()
        # self.find_element(Locator_GR1.locator_search_group).click() #ссылка к локатору
        self.find_element(Locator_GR1.locator_user_add_group).click()
        self.find_element(Locator_GR1.locator_save).click()

    def get_user_two(self):
        self.find_element(Locator_GR1.locator_add_user).click()
        self.find_element(Locator_GR1.locator_username).send_keys(Data.add_user_two)
        self.find_element(Locator_GR1.locator_userpass).send_keys(Data.password_us_two)
        self.find_element(Locator_GR1.locator_userpass_confirm).send_keys(Data.password_us_two)
        self.find_element(Locator_GR1.locator_continue).click()
        self.find_element(Locator_GR1.locator_id_staff).click()
        self.find_element(Locator_GR1.locator_id_superuser).click()
        self.find_element(Locator_GR1.locator_save).click()
        # self.find_element(Locator_GR1.locator_continue).click()

    def log_out(self):
        log_out = self.find_element(Locator_GR2.locator_log_out)
        return log_out

    def post_page(self):
        post = self.find_element((By.CSS_SELECTOR, '#content-main > div.app-app.module > table > tbody > tr > th > a'))
        return post

    def delete_post(self):
        checkboxes = self.find_elements((By.NAME, '_selected_action'))
        checkboxes[-1].click()
        select = Select(self.find_element((By.NAME, 'action')))
        select.select_by_value('delete_selected')
        self.find_element((By.NAME, 'index')).click()
        self.find_element((By.CSS_SELECTOR, '#content > form > div > input[type=submit]:nth-child(4)')).click()

    def user_data(self):
        data_user = self.find_elements(Locator_GR1.locator_user_data)
        nav_bar_menu = [x.text for x in data_user if len(x.text) > 0]
        return nav_bar_menu

    # def cart_page(self):
    #     self.find_element(Locator.locator_two).click()
    #     search_card = self.find_element(Locator.locator_tree).text
    #     return search_card
    #
    # def card_empty(self):
    #     self.find_element(Locator.locator_two).click()
    #     search_empty = self.find_element(Locator.locator_empty).text
    #     return search_empty
    #
    # def admin_page(self):
    #     self.find_element(Locator.locator_login).click()
    #     login_page = self.find_element(Locator.locator_login_confirm).text
    #     return login_page
    #
    # def closes(self):
    #     all_list = self.find_elements(Locator.locator_closes)
    #     nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
    #     return nav_bar_menu

    # def check_navigation_bar(self):
    #     all_list = self.find_elements(Locator.locator_One, time=2)
    #     nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
    #     print(nav_bar_menu)
    #     return nav_bar_menu
