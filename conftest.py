import os
import pytest
from selenium import webdriver
from settings.config import get_driver_path


@pytest.fixture
def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    get_driver_path()   # local enviroment variables are enabled

    driver = webdriver.Chrome(options=options, executable_path=os.getenv('CHROME_PATH'))
    driver.get('https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all')

    yield driver

    driver.close()
