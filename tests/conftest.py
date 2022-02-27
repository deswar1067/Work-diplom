import psycopg2
import pytest
# from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from selenium import webdriver


@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.maximize_window()
   

    yield driver

    driver.quit()


@pytest.fixture
def create_connection():
    # try:
        connection = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        yield cursor
        cursor.close()
        connection.close()
        print("Connection to Postgres DB seccessful")
        # return cursor

    # except Error as e:
    #     print(f'Connection error "{e}" occured')


